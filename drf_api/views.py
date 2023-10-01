""" Views for the drf_api project. """
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
    JWT_AUTH_COOKIE, JWT_AUTH_REFRESH_COOKIE,
    JWT_AUTH_SAMESITE, JWT_AUTH_SECURE,
)


@api_view()
def root_view(request):
    """Root endpoint for the --Dishcovery-- drf_api project."""
    return Response(
        {
            "message": "Welcome to the Dishcovery API! We're so excited to have you join our community of food lovers 🍽️."
        }
    )


@api_view(["POST"])
def logout_view(request):
    """View to logout a user."""
    response = Response()
    response.set_cookie(
        JWT_AUTH_COOKIE,
        value="", max_age=0, httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value="",
        httponly=True,
        expires="Thu, 01 Jan 1970 00:00:00 GMT",
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response
