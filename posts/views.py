"""This module contains the views for the posts app."""
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serialiazers import PostSerializer


# Create your views here.
class PostList(APIView):
    """Post list view."""
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        """Get method."""
        posts = Post.objects.all()  # pylint: disable=no-member
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request):
        """Post method."""
        serializer = PostSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def put(self, request):
    #     """Put method."""
    #     post = Post.objects.get(id=request.data["id"])  # pylint: disable=no-member
    #     serializer = PostSerializer(post, data=request.data, context={"request": request})
    #     if serializer.is_valid():
    #         serializer.save(owner=request.user)
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def delete(self, request):
    #     """Delete method."""
    #     post = Post.objects.get(id=request.data["id"])  # pylint: disable=no-member
    #     post.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
