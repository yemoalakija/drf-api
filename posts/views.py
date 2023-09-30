"""This module contains the views for the posts app."""
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


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


class PostDetail(APIView):
    """Post detail view."""
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, primary_key):
        """Get object."""
        try:
            post = Post.objects.get(pk=primary_key)  # pylint: disable=no-member
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist as exc:  # pylint: disable=no-member
            raise Http404 from exc

    def get(self, request, primary_key):
        """Get method."""
        post = self.get_object(primary_key)
        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data)

    def put(self, request, primary_key):
        """Put method."""
        post = self.get_object(primary_key)
        serializer = PostSerializer(post, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,primary_key):
        """Delete method."""
        post = self.get_object(primary_key)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
