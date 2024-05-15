from django.contrib import admin
from .models import Article, Ip

# Register your models here.
# @admin.register(Article)
# class ArticleAdmin(admin.ModelAdmin):
#     pass
admin.site.register(Article)
admin.site.register(Ip)