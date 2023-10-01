""" Views for the drf_api project. """
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_view(request):
    """Root endpoint for the --Dishcovery-- drf_api project."""
    return Response(
        {
            "message": "Welcome to the Dishcovery API! We're so excited to have you join our community of food lovers 🍽️."
        }
    )
