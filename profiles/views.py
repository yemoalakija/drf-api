"""Profiles views."""
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer


# Create your views here.
class ProfileList(APIView):
    """Profile list."""

    def get(self, request):
        """Get."""
        profiles = Profile.objects.all()  # pylint: disable=no-member
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)
