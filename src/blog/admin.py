from django.contrib import admin
from blog.models import Author, Category, Post 

# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)