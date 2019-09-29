from django.contrib import admin

# Register your models here.
from .models import Posts, Comment

admin.site.register(Posts)
admin.site.register(Comment)
