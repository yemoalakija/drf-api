"""Comments serializers."""
from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


# Create your serializers here.
class CommentSerializer(serializers.ModelSerializer):
    """Comment serializer."""

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """Get is owner."""
        request = self.context["request"]
        return request.user == obj.owner

    def get_created_at(self, obj):
        """Get created at."""
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """Get updated at."""
        return naturaltime(obj.updated_at)

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
