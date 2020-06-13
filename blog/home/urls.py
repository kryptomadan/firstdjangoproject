from django.urls import path
from . import views
from .views import PostListView,PostdetailView,PostcreateView,PostupdateView,PostdeleteView


urlpatterns = [
    path('',PostListView.as_view(),name="blog-home"),
    path('posts/<int:pk>',PostdetailView.as_view(),name="posts-detail"),
    path('posts/new',PostcreateView.as_view(),name="posts-create"),
    path('posts/<int:pk>/update',PostupdateView.as_view(),name="posts-update"),
    path('posts/<int:pk>/delete',PostdeleteView.as_view(),name="posts-delete"),
 
]

app_name = 'home'