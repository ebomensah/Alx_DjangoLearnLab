from django.urls import path
from .views import list_books, LibraryListView 
from . import views

urlpatterns=[
    path('list_books/', list_books, name = 'list_books'),
    path('library_detail/', LibraryListView.as_view(), name = 'library_detail'),
    path('register/', views.register_view, name = 'register'),
    path('index/', views.index_view, name = 'index'),
    path('userlogin/', views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', views.LogoutView.as_view(template_name="logout.html"), name = 'logout'),
    path('myadmin/', views.myadmin_view, name='myadmin_view'),
    path('librarian/', views.librarian_view, name='librarian_view'),
    path('member/', views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]
