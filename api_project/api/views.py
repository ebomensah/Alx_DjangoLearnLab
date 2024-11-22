from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from turtle import title
from django.shortcuts import redirect, render
from rest_framework.mixins import Response
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework import viewsets, generics
from .models import Book
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import obtain_auth_token, APIView
from django.contrib.auth.models import User 
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.views import LoginView, LogoutView


class BookList (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        title_filter = self.request.query_params.get('title', None)
        if title_filter is not None:
            queryset = queryset.filter (title__icontains=title_filter)
        return queryset 
# Create your views here.

class BookViewSet(viewsets.ModelViewSet):

    #A viewset for viewing and editing your models.
    #Authentication is required to access this endpoint. Only authenticated users 
    #can view and edit models. Admin users are the only ones allowed to delete.
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    #This function applies specific permissions to different actions:
     #   - Only admins can delete resources.
      #  - All authenticated users can read and modify.
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Book.objects.filter(user=self.request.user)


class SwitchUserTokenView(APIView):
    """
    This view allows an authenticated user to switch to another user's token.
    It requires the username and password of the other user.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username = username)
            if user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            
            else:
                return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

from .forms import UserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate (username=username, password=password)
            login (request, user)
            return redirect ('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render (request, 'api/register.html', context)

class LoginView(LoginView):
    template_name = 'accounts/login.html'
 

class LogoutView(LogoutView):
    next_page = 'login'
def index_view(request):
    return render (request, 'api/books.html')

