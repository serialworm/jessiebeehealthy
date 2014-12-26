from django.shortcuts import render
from blog.models import Category, Page, Post


def index(request):
    page = Page.objects.get(name='home')
    print('page: ')
    print(page)
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
