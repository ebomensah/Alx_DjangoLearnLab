from turtle import title
from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework import viewsets, generics
from .models import Book

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
    queryset = Book.objects.all()
    serializer_class = BookSerializer

