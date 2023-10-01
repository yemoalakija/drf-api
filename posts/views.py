"""This module contains the views for the posts app."""
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    """Post list view."""
    queryset = Post.objects.all()  # pylint: disable=no-member
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetail(generics.RetrieveDestroyAPIView):
    """Post detail view."""
    queryset = Post.objects.all()  # pylint: disable=no-member
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
