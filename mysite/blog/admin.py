from django.contrib import admin
from blog.models import Author, Category, Page, Post

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)


class PageAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')

admin.site.register(Page, PageAdmin)
