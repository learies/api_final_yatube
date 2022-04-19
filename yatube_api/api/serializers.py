from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post

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
