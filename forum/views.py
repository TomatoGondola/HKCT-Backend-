from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "forum/forum.html")

def forum(request):
    return render(request, "forum/forum.html")
# articles doesn't render article.html but article_page

def forum_thread(request):
    return render(request, "forum/forum_thread.html")

def thread(request):
    return render(request, "forum/thread.html")