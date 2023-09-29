"""Profiles views."""
from django.http import Http404
from rest_framework import status
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


class ProfileDetail(APIView):
    """Profile detail."""
    serializer_class = ProfileSerializer
    def get_object(self, primary_key):
        """Get object."""
        try:
            profile = Profile.objects.get(pk=primary_key)  # pylint: disable=no-member
            return profile
        except Profile.DoesNotExist as exc:  # pylint: disable=no-member
            raise Http404 from exc

    def get(self, request, primary_key):
        """Get."""
        profile = self.get_object(primary_key)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, primary_key):
        """Put."""
        profile = self.get_object(primary_key)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, primary_key):
        """Delete."""
        profile = self.get_object(primary_key)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
