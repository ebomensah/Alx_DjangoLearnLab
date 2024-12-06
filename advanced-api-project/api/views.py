from django.shortcuts import render
from django.views import generic
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticated

class BookListView(generic.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # No authentication required for listing

class BookDetailView(generic.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []  # No authentication required for retrieving details
# Create your views here.

class BookCreateView(generic.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create

class BookUpdateView(generic.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update

    def perform_update(self, serializer):
        instance = serializer.save()

class BookDeleteView(generic.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete
