"""Posts models."""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """Post model."""
    image_filter_choices = [
        ('_2023', '2023'),
        ('9jadishcovery🏁', 'Nigeria'),
        ('gbdishcovery', 'British'),
        ('chndishcovery', 'China'),
        ('francedishcovery', 'France'),
        ('spndishcovery', 'Spanish'),
        ('jpdishcovery', 'Japan'),
        ('inddishcovery', 'India'),
        ('grcdishcovery', 'Greece'),
        ('thndishcovery', 'Thailand'),
        ('turkdishcovery', 'Turkey'),
        ('usadishcovery', 'USA'),
        ('mexdishcovery', 'Mexico'),
        ('itadishcovery', 'Italy')
    ]

    # Sort the choices alphabetically
    image_filter_choices = sorted(image_filter_choices, key=lambda x: x[1])

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(
        upload_to="images/", default="../default_post_izrxi1", blank=True, null=True
    )
    image_filter = models.CharField(
        max_length=50, choices=image_filter_choices, default="normal"
    )

    class Meta:
        """Meta class."""

        ordering = ["-created_at"]

    def __str__(self):
        """Return name."""
        return f"{self.id} {self.title}"  # pylint: disable=no-member
