
from django.urls import path
from .views import PostListView, PostDetailView,PostEditView,PostDeleteView,CommentDeleteView,ProfileView,AddLike,AddDislike,Code
urlpatterns = [
    path('post', PostListView.as_view(), name='post-list'),
    path('post/code',Code.as_view(), name='code'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:pk>/dislike', AddDislike.as_view(), name='dislike'),
    path('post/edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
]
