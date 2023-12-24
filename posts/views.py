from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from social.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    
