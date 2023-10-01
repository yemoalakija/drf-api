"""URLs for the likes app."""
from django.urls import path
from likes import views

# Create your views here.
urlpatterns = [
    path("likes/", views.LikeList.as_view()),
    path("likes/<int:pk>/", views.LikeDetail.as_view()),
]
