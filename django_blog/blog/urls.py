from django.urls import path, include
from .views import LoginView, LogoutView, RegisterView, ProfileView, UserUpdateView, ProfileUpdateView
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update_user/', UserUpdateView.as_view(), name='update_user'),
    path('update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
    path('posts/', PostListView.as_view(), name = 'post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('posts/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-edit'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('posts/<int:post_id>/comments/new/', add_comment, name='add-comment'),
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]