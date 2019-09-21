from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Posts(models.Model):
    author = models.ForeignKey(User,models.SET_NULL,blank=True,null=True,)
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    body = models.TextField()
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', default = '', blank=True, null=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', default = '', blank=True, null=True)
    photo_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', default = '', blank=True, null=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', default = '', blank=True, null=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', default = '', blank=True, null=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', default = '', blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"

    # model method for showing first line of body 
    def snippet(self):
        if len(self.body) > 150:
            return self.body[:150] + "..."
        else :
            return self.body
