from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404
from django.core.cache import cache

# Create your views here.

# Метод для получения айпи
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

def index(request):
    articles = Article.objects.all().order_by('-id')
    ip = get_client_ip(request)
    
    for article in articles:
        article.view_count_text = get_view_count_text(article.view_count)

    context = {"articles": articles} 
    return render(request, "index.html", context)

def get_view_count_text(view_count):
    if view_count % 10 == 1 and view_count % 100 != 11:
        return f"{view_count} просмотр"
    elif 2 <= view_count % 10 <= 4 and (view_count % 100 < 10 or view_count % 100 >= 20):
        return f"{view_count} просмотра"
    else:
        return f"{view_count} просмотров"
    

def article_page(request, slug):
    article = get_object_or_404(Article, slug=slug)

    # Increment the view count for the article
    ip_address = get_client_ip(request)
    cache_key = f"article_{article.id}_view_count_{ip_address}"
    if not cache.get(cache_key):
        article.view_count += 1
        article.save()
        cache.set(cache_key, True, 360)  # Cache the view for 10 mins

    view_count_text = get_view_count_text(article.view_count)

    context = {"article": article, "view_count_text": view_count_text}
    return render(request, "article_page.html", context)



def custom_404_view(request, exception):
    return render(request, '404.html', status=404)



