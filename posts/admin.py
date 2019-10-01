from django.contrib import admin

# Register your models here.
from .models import Posts, Comment, PostCategory, ItemsList

admin.site.register(Posts)
admin.site.register(Comment)

admin.site.register(PostCategory)
admin.site.register(ItemsList)
