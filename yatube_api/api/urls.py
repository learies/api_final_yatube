from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet

v1_router = DefaultRouter()

v1_router.register('posts', PostViewSet, basename='post')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
