""" Custom serializers for the drf_api app. """
from rest_framework import serializers
from dj_rest_auth.serializers import UserDetailsSerializer


class CurrentUserSerializer(UserDetailsSerializer):
    """ Custom serializer to return current user profile image. """
    profile_id = serializers.ReadOnlyField(source="profile.id")
    profile_image = serializers.ReadOnlyField(source="profile.image.url")

    class Meta(UserDetailsSerializer.Meta):
        """ Add profile_id and profile_image to the default fields. """
        fields = UserDetailsSerializer.Meta.fields + (
            "profile_id", "profile_image"
        )
