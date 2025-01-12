from tokenize import Comment
from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Post, Comment
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    authentication_classes = [TokenAuthentication]
    filterset_fields = ['title', 'content', 'author']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated,IsAuthorOrReadOnly]
    authentication_classes = [TokenAuthentication]

class FeedView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        followed_users = request.user.following.all()
        
        if not followed_users:
            return Response({"detail": "You are not following anyone."}, status= 200)

        posts = Post.objects.filter(author__in=followed_users.values('id')).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response (serializer.data)




#class CreatePostView(generics.CreateAPIView):
 #   serializer_class = PostSerializer
  #  permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

#class EditPostView(generics.UpdateAPIView):
 #   serializer_class = PostSerializer
  #  permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

#class ViewPostView(generics.ListAPIView):
 #   serializer_class = PostSerializer
#    permission_classes = [permissions.IsAuthenticated]

#class DeletePostView(generics.DestroyAPIView):
 #   serializer_class = PostSerializer
  #  permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]



#class CreateCommentView(generics.CreateAPIView):
 #   serializer_class = CommentSerializer
  #  permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

#class EditCommentView(generics.UpdateAPIView):
 #   serializer_class = CommentSerializer
  #  permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

#class ViewCommentView(generics.ListAPIView):
 #   serializer_class = CommentSerializer
  #  permission_classes = [permissions.IsAuthenticated]

#class DeleteCommentView(generics.DestroyAPIView):
 #   serializer_class = PostSerializer
  #  permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


 

# Create your views here.
