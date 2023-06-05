from django.urls import path
from .views import render_Post, post_detail 


app_name = 'blog'

urlpatterns = [
    path('',render_Post, name='Post'),
    path('<int:post_id>', post_detail, name='post_detail'),
]


