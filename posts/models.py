from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class PostCategory(models.Model):

    category_name = models.CharField(max_length=200)
    category_slug = models.SlugField(default=1)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class ItemsList(models.Model):
    ItemsList_name = models.CharField(max_length=200)
    item_category = models.ForeignKey(PostCategory,
                                      default=1,
                                      verbose_name="Category",
                                      on_delete=models.SET_DEFAULT)

    item_summary = models.CharField(max_length=200)
    rating = models.DecimalField(decimal_places=1, max_digits=2)
    numcomment = models.DecimalField(decimal_places=4, max_digits=5, null=True, blank=True, default=None)

    class Meta:
        # otherwise we get "Tutorial Seriess in admin"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.ItemsList_name


class Posts(models.Model):
    author = models.ForeignKey(User,
                               models.SET_NULL,
                               blank=True,
                               null=True,
                               related_name='posted')

    post_item = models.ForeignKey(ItemsList,
                                  default=1,
                                  verbose_name="Posts",
                                  on_delete=models.SET_DEFAULT)

    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()

    likes = models.ManyToManyField(User,
                                   blank=True,
                                   related_name='likes')

    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default='', blank=True, null=True)
    photo_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default='', blank=True, null=True)
    photo_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default='', blank=True, null=True)
    photo_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default='', blank=True, null=True)
    photo_5 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default='', blank=True, null=True)
    photo_6 = models.ImageField(
        upload_to='photos/%Y/%m/%d/', default='', blank=True, null=True)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"

    # Count total number of likes
    def total_likes(self):
        return self.likes.count()

    # model method for showing first line of body
    def snippet(self):
        if len(self.body) > 150:
            return self.body[:150] + "..."
        else:
            return self.body


class Comment(models.Model):
    post = models.ForeignKey('Posts', models.SET_NULL,
                             blank=True, null=True, related_name='comments',)
    author = models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name='authcomments')
    text = models.TextField()
    scores = models.DecimalField(decimal_places=1, max_digits=2, null=True, blank=True, default=None)
    created_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.text
