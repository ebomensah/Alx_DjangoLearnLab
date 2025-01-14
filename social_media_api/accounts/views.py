from http.client import CREATED
from rest_framework import generics, permissions, status
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.decorators import action

class profile_view(TemplateView):
    template_name = 'accounts/profile.html'

class UserRegistrationView(generics.CreateAPIView):
    serializer_class= CustomUserSerializer
    permission_classes= [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer= CustomUserSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                'user': serializer.data,
                'token': token.key
            }, status=status .HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request):
        return Response({'message': 'Send a POST request with credentials to log in.'})
    
    def post(self, request):
        #print(request.data)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token':token.key})
        else:
            return Response({'error':'Invalid credentials'}, status=401)

class LogoutView(APIView):
    next_page = 'login'

class FollowUserView(generics.GenericAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @action (detail=True, methods={'post'})
    def follow_user(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow == request.user:
           return Response ({"detail": "You cannot follow yourself"}, status = 400)    
        
        request.user.following.add(user_to_follow)
        return Response({"detail": f"Successfully followed {user_to_follow.username}"}, status =200)


class UnfollowUserView(generics.GenericAPIView):
    queryset=CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @action (detail=True, methods={'post'})
    def unfollow_user(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)

        if user_to_unfollow == request.user:
            return Response({"detail": "You cannot unfollow yourself."}, status=400)
        
        # Unfollow the user
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"Successfully unfollowed {user_to_unfollow.username}"}, status=200)
# Create your views here.
