from django.shortcuts import render
from .models import Article



# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "index.html", context)

def article_page(request, slug):
    article = Article.objects.get(slug=slug)
    context = {"article": article}
    return render(request, "article_page.html", context)























