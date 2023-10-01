# pylint: disable=no-member
"""This module contains the views for the posts app."""
from django.db.models import Count
from rest_framework import generics, permissions, filters
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


# Create your views here.
class PostList(generics.ListCreateAPIView):
    """Post list view."""
    queryset = Post.objects.annotate(
        likes_count=Count("likes", distinct=True),
        comments_count=Count("comment", distinct=True),
    ).order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ["owner__username", "title",]
    ordering_fields = [
        "likes_count",
        "comments_count",
        "likes__created_at",
    ]

    def perform_create(self, serializer):
        """Perform create."""
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveDestroyAPIView):
    """Post detail view."""
    queryset = Post.objects.annotate(
        likes_count=Count("likes", distinct=True),
        comments_count=Count("comment", distinct=True),
    ).order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
