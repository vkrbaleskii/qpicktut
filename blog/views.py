from django.shortcuts import render
from .models import Posts


def index(request):
    # return HttpResponse("Hello, world. You're at the blog index.")

    posts = Posts.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html ', context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }

    return render(request, 'posts/details.html ', context)
