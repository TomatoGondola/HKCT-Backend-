from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "articles/articles.html")

def articles(request):
    return render(request, "articles/articles.html")
# articles doesn't render article.html but article_page

def article_page(request):
    return render(request, "articles/article_page.html")