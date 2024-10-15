from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "careers/careers.html")

def careers(request):
    return render(request, "careers/careers.html")
# articles doesn't render article.html but article_page

def career_page(request):
    return render(request, "careers/career_page.html")