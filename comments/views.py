"""Comments views."""
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# Create your views here.
class CommentList(generics.ListCreateAPIView):
    """Comment list view."""
    queryset = Comment.objects.all()  # pylint: disable=no-member
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Perform create."""
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """Comment detail view."""
    queryset = Comment.objects.all()  # pylint: disable=no-member
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]
