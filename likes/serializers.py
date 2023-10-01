"""Likes serializers."""
from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


# Create your serializers here.
class LikeSerializer(serializers.ModelSerializer):
    """Like serializer."""

    owner = serializers.ReadOnlyField(source="owner.username")


    class Meta:
        """Meta class."""

        model = Like
        fields = ["id", "owner", "created_at", "post"]
        read_only_fields = ["created_at"]

    def create(self, validated_data):
        """Create method."""
        try:
            return super().create(validated_data)
        except IntegrityError as exc:
            raise serializers.ValidationError({"detail": "You already liked this post!"}) from exc
