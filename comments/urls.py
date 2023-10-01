"""URLs for the comments app."""
from django.urls import path
from comments import views


# Create your views here.
urlpatterns = [
    path("comments/", views.CommentList.as_view()),
    path("comments/<int:pk>/", views.CommentDetail.as_view()),
]
