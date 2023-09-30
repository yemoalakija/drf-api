# pylint: disable=no-member
"""Posts tests."""
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostListViewTests(APITestCase):
    """Post list view test."""

    def setUp(self):
        """Set up."""
        User.objects.create_user(username="testuser", password="password")

    def test_post_list(self):
        """Test get post list."""
        testuser = User.objects.get(username="testuser")
        Post.objects.create(owner=testuser, title="Test post", content="Test content")
        response = self.client.get("/posts/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        """Test logged in user can create post."""
        self.client.login(username="testuser", password="password")
        response = self.client.post(
            "/posts/",
            {"title": "Test post", "content": "Test content"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, "Test post")
        self.assertEqual(Post.objects.get().content, "Test content")

    def test_logged_out_user_cannot_create_post(self):
        """Test logged out user cannot create post."""
        response = self.client.post(
            "/posts/",
            {"title": "Test post", "content": "Test content"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 0)
