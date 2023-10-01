"""Defines URL patterns for followers."""
from django.urls import path
from followers import views

# Create your views here.
urlpatterns = [
    path("followers/", views.FollowerList.as_view()),
    path("followers/<int:pk>/", views.FollowerDetail.as_view()),
]
