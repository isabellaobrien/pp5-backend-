from rest_framework import generics, permissions
from social.permissions import IsOwnerOrReadOnly
from .models import CommentLike
from .serializers import CommentLikeSerializer

class CommentLikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = CommentLikeSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = CommentLike.objects.all()

