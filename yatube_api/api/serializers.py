from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post, User

AUTHOR = SlugRelatedField(slug_field='username', read_only=True)


class PostSerializer(serializers.ModelSerializer):
    author = AUTHOR

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'group')
        read_only_fields = ('id', 'pub_date', 'author')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug')
        read_only_fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    author = AUTHOR

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('id', 'author', 'created')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    def validate(self, data):
        user = get_object_or_404(User, username=data.get('following').username)
        follow = Follow.objects.filter(
            user=self.context.get('request').user, following=user).exists()
        if user == self.context.get('request').user:
            raise serializers.ValidationError(
                'Вы не можете подписаться сам на себя')
        if follow is True:
            raise serializers.ValidationError(
                'Вы уже подписаны на пользователя')
        return data

    class Meta:
        model = Follow
        fields = ('id', 'user', 'following')
