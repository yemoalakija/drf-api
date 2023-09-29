"""Permissions for the API."""
from rest_framework import permissions


# Create your permissions here.
class IsOwnerOrReadOnly(permissions.BasePermission):
    """Is owner or read only."""

    def has_object_permission(self, request, view, obj):
        """Has object permission."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
