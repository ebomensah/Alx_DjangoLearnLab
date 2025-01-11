from django.views import generic
from .models import Book, User, BlogPost
from .serializers import BookSerializer, UserSerializer, BlogPostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from rest_framework import generics, filters, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from rest_framework.decorators import action
from rest_framework.response import Response

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr='icontains')
    publication_year = django_filters.NumberFilter()

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # No authentication required for listing
    filter_backends= [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['title']



class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # No authentication required for retrieving details
# Create your views here.

class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

    def perform_update(self, serializer):
        instance = serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete

class BlogPostListView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    @action (detail=True, methods=['post'])
    def like(self, request, pk=None):
        blog_post = self.get_object()
        blog_post.likes += 1
        blog_post.save()
        return Response({'status': 'liked', 'likes': blog_post.likes})
    
class BlogPostCreateView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer