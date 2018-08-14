from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Category, Post


def home(request):

    #Category.objects.create(name='Python')
    categories = Category.objects.all()

    category_python = Category.objects.get(id=1)
    posts = Post.objects.all()

    # post = Post()
    # post.name = 'show post 3'
    # post.content = 'Content'
    # post.status = 'Draft'
    # post.category = category_python

    nome = 'Bruno'
    context = {
        'name': nome,
        'categories': categories,
        'posts': posts,
    }

    return render(request, 'blog/home.html', context)