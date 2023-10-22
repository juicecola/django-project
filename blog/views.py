from django.shortcuts import render
from .models import Post


def home(request):
    posts = Post.objects.all()  # Retrieve all Post objects from the database
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
# Create your views here.
