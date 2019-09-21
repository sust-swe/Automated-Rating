from django.db import models
from datetime import datetime

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField()
    body = models.TextField()
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
