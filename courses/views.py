from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "courses/courses.html")

def courses(request):
    return render(request, "courses/courses.html")
# articles doesn't render article.html but article_page

def course_page(request):
    return render(request, "courses/course_page.html")