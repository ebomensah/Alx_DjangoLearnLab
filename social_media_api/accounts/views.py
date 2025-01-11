from http.client import CREATED
from rest_framework import generics, permissions, status
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test, permission_required
from django.shortcuts import redirect, render
from django.contrib.auth.views import LogoutView
from .forms import CustomUserCreationForm
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response 
from .serializers import UserSerializer

class profile_view(TemplateView):
    template_name = 'accounts/profile.html'

class UserRegistrationView(generics.CreateAPIView):
    serializer_class= UserSerializer
    permission_classes= [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer= UserSerializer(data=request.data)

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



# Create your views here.
