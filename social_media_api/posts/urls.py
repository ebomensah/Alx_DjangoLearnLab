from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView
from rest_framework.routers import DefaultRouter

    #path('posts/createpost', views.CreatePostView.as_view(), name = 'posts'),
    #path('posts/editpost/<slug:slug>', views.EditPostView.as_view(), name = 'edit-posts'),
    #path('posts/listpost', views.ViewPostView.as_view(), name = 'view-posts'),
    #path('posts/deletepost/<slug:slug>', views.DeletePostView.as_view(), name = 'delete-posts'),
    #path('posts/createcomment', views.CreateCommentView.as_view(), name = 'create-comment'),
    #path('posts/editcomment/<slug:slug>', views.EditCommentView.as_view(), name = 'edit-comment'),
    #path('posts/viewcomment', views.ViewCommentView.as_view(), name = 'view-comment'),
    #path('posts/deletecomment/<slug:slug>', views.DeleteCommentView.as_view(), name = 'delete-comment'),
    


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')


urlpatterns = [
    path('', include(router.urls)),
    path('feed/', FeedView.as_view(), name='feed'),
]

