"""Comments serializers."""
from rest_framework import serializers
from .models import Comment


# Create your serializers here.
class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer."""

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source="owner.profile.id")
    profile_image = serializers.SerializerMethodField(source="owner.profile.image.url")

    def get_is_owner(self, obj):
        """Get is owner."""
        request = self.context["request"]
        return request.user == obj.owner

    def get_profile_id(self, obj):
        """Get profile id."""
        return obj.owner.profile.id

    def get_profile_image(self, obj):
        """Get profile image."""
        return obj.owner.profile.image.url

    class Meta:
        """Meta class."""

        model = Comment
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "post",
            "created_at",
            "updated_at",
            "content",
        ]


class CommentDetailSerializer(CommentSerializer):
    """Comment detail serializer."""
    post = serializers.ReadOnlyField(source="post.id")
