from django.db import models
from datetime import datetime
from django.urls import reverse

# Create your models here.

class Ip(models.Model): # наша таблица где будут айпи адреса
    ip = models.CharField(max_length=100)
    
    def __str__(self):
        return self.ip

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=255, unique=True)
    views = models.ManyToManyField(Ip, related_name="post_views", blank=True)
    

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_page", kwargs={"slug": self.slug})
    def total_views(self):
        return self.views.count()
    

