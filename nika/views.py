from django.shortcuts import render
from .models import Article,Ip



# Create your views here.

# Метод для получения айпи
def get_client_ip(request):
    x_real_ip = request.META.get('HTTP_X_REAL_IP')
    if x_real_ip:
        ip = x_real_ip
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "index.html", context)

def article_page(request, slug):
    article = Article.objects.get(slug=slug)

    ip = get_client_ip(request)

    # if Ip.objects.filter(ip=ip).exists():
    #     Article.views.add(Ip.objects.get(ip=ip))
    # else:
    #     Ip.objects.create(ip=ip)
    #     Article.views.add(Ip.objects.get(ip=ip))

    Ip.objects.get_or_create(ip=ip)

    context = {"article": article}
    return render(request, "article_page.html", context)



