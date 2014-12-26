from django.contrib import admin
from blog.models import Author, Category, Page, Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Post)
