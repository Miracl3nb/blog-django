from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def render_Post(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts' : posts})



def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})