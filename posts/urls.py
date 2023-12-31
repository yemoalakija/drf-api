"""Posts URLs."""
from django.urls import path
from posts import views

# Create your views here.
urlpatterns = [
    path("posts/", views.PostList.as_view()),
    path("posts/<int:pk>/", views.PostDetail.as_view()),
]
