"""Followers views."""
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


# Create your views here.
class FollowerList(generics.ListCreateAPIView):
    """Follower list view."""

    queryset = Follower.objects.all()  # pylint: disable=no-member
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Perform create."""
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """Follower detail view."""

    queryset = Follower.objects.all()  # pylint: disable=no-member
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
