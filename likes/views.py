"""Likes views."""
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer


# Create your views here.
class LikeList(generics.ListCreateAPIView):
    """Like list view."""
    queryset = Like.objects.all()  # pylint: disable=no-member
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Perform create."""
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """Like detail view."""
    queryset = Like.objects.all()  # pylint: disable=no-member
    serializer_class = LikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
