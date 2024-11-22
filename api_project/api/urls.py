from os import name
from django.urls import path, include
from rest_framework.routers import DefaultRouter 
from .views import BookList, BookViewSet, SwitchUserTokenView
from rest_framework.authtoken.views import obtain_auth_token
from .views import LoginView, LogoutView, register_view

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name = 'book-list'),
    path('api', include(router.urls)),
    path('api-token-auth/', obtain_auth_token),
    path('switch_user/', SwitchUserTokenView.as_view(), name = 'switch_user'),
    path('login/', LoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
    path('register/', register_view, name = 'register'),
]
