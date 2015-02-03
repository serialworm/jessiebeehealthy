from django.shortcuts import render, get_object_or_404
from blog.models import Category, Page, Post


def index(request):
    page = Page.objects.get(slug='home')
    title = page.title
    description = page.description
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'title': title,
        'description': description,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'index.html', {'page': context})


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    title = category.title
    description = category.description
    posts = Post.objects.get(category=category)
    categories = Category.objects.all()
    context = {
        'title': title,
        'description': description,
        'posts': posts,
        'categories': categories
    }
    return render(request, 'category.html', {'page': context})
