from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    path('user/', views.UserListView.as_view(), name='user-list'),
    path('blogpost/', views.BlogPostListView.as_view(), name='blogs'),
    path('blogpost/create/', views.BlogPostCreateView.as_view(), name='blogs-create'),
]