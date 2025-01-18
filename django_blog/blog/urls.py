from django.urls import path, include
from .views import LoginView, LogoutView, RegisterView, ProfileView, UserUpdateView, ProfileUpdateView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update_user/', UserUpdateView.as_view(), name='update_user'),
    path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
    path('posts/', PostListView.as_view(), name = 'post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('posts/new/', PostCreateView.as_view(), name = 'post-create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name = 'post-edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
]