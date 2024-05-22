from django.db import models
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.dispatch import receiver


class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    full_text = models.TextField()
    category = models.CharField(max_length=255)
    pubdate = models.DateTimeField()
    slug = models.CharField(max_length=255, unique=True)    
    view_count = models.IntegerField(default=0)
    og_image = models.ImageField(upload_to="images", null=True, blank=True)
    

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_page", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
            
            if self.id:
                existing = get_object_or_404(Article, id=self.id)
                if existing.og_image != self.og_image:
                    existing.og_image.delete(save=False)

            super(Article, self).save(*args, **kwargs)

    @receiver(models.signals.pre_delete, sender="nika.Article")
    def server_delete_files(sender, instance, **kwargs):

        if instance.id is not None:
            for field in instance._meta.fields:
                if field.name == "og_image":
                    file = getattr(instance, field.name)
                    if file:
                        file.delete(save=False)