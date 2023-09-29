"""URLs module for the profiles app."""
from django.urls import path
from profiles import views

urlpatterns = [
    path("profiles/", views.ProfileList.as_view()),
    path("profiles/<int:primary_key>/", views.ProfileDetail.as_view()),
]
