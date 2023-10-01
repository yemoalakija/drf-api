"""Profiles views."""
from rest_framework import generics
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileList(generics.ListAPIView):
    """Profile list."""
    queryset = Profile.objects.all()  # pylint: disable=no-member
    serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """Profile detail."""
    queryset = Profile.objects.all()  # pylint: disable=no-member
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
