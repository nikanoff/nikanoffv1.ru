from django.db import models
from datetime import datetime
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=255, unique=True)    
    view_count = models.IntegerField(default=0)
    

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_page", kwargs={"slug": self.slug})
    
    

