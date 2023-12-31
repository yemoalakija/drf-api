"""Posts serializers."""
from rest_framework import serializers
from likes.models import Like
from .models import Post


# Create your serializers here.
class PostSerializer(serializers.ModelSerializer):
    """Post serializer."""

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.SerializerMethodField(source="owner.profile.id")
    profile_image = serializers.SerializerMethodField(source="owner.profile.image.url")
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """Validate image."""
        if value:
            if value.size > 1024 * 1024 * 2:
                raise serializers.ValidationError("Image size too large!")
            # if value.image.format not in [".png", ".jpg", ".jpeg"]:
            #     raise serializers.ValidationError("Image format not supported!")
            if value.image.width > 4096 or value.image.height > 4096:
                raise serializers.ValidationError("Image resolution larger than 4096px!")
        return value

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

    def get_like_id(self, obj):
        """Get like id."""
        user = self.context["request"].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, post=obj).first()  # pylint: disable=no-member
            return like.id if like else None
        return None

    class Meta:
        """Meta class."""

        model = Post
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "created_at",
            "updated_at",
            "title",
            "content",
            "image",
            "image_filter",
            "like_id",
            "likes_count",
            "comments_count",
        ]
