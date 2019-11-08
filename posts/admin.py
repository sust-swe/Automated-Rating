from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import Posts, Comment, PostCategory, ItemsList


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_item', 'snippet', 'author')
    list_filter = ('created_at', 'post_item',)


admin.site.register(Posts, PostsAdmin)
admin.site.register(Comment)

admin.site.register(PostCategory)
admin.site.register(ItemsList)

admin.site.unregister(Group)
