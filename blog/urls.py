from django.urls import path
from .views import *
urlpatterns = [
    path('',posts,name='posts'),
    path('posts/<int:pk>',post_details,name='post_details'),
    path('posts/create',create_post,name='create_post'),
    path('posts/<int:pk>/delete',delete_post,name="delete_post")
]
