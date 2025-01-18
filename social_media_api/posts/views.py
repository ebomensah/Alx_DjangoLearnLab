from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly
from .models import Post, Comment, Like
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import models 

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
        following_users = request.user.following.all()
        
        if not following_users:
            return Response({"detail": "You are not following anyone."}, status= 200)

        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        serializer = PostSerializer(posts, many=True)
        return Response (serializer.data)

#@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)

   # if created:
  #      Notification.objects.create(
  #          recipient=post.author,  # Assuming Post has an author field
   #         actor=request.user,
    #        verb='liked your post',
     #       target=post
      #  )
       # return Response({'message': 'Post liked.'}, status=status.HTTP_201_CREATED)
    #return Response({'message': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['DELETE'])
#@permission_classes([IsAuthenticated])
#def unlike_post(request, pk):
 #   post = Post.objects.get(pk=pk)
  #  try:
   #     like = Like.objects.get(user=request.user, post=post)
    #    like.delete()
     #   return Response({'message': 'Post unliked.'}, status=status.HTTP_204_NO_CONTENT)
    #except Like.DoesNotExist:
    #    return Response({'message': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
        

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
