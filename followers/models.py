"""Followers models."""
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Follower(models.Model):
    """Follower model."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class."""

        ordering = ["-created_at"]
        unique_together = ["owner", "followed"]

    def __str__(self):
        """Return name."""
        return f"{self.owner} {self.followed}"  # pylint: disable=no-member
