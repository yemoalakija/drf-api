"""Profiles serializers."""
from rest_framework import serializers
from .models import Profile


# Create your serializers here.
class ProfileSerializer(serializers.ModelSerializer):
    """Profile serializer."""
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Get is owner."""
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        """Meta class."""

        model = Profile
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "name",
            "content",
            "image",
            "is_owner",
        ]
