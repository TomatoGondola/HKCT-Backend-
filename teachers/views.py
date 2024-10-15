from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "teachers/teacher_registration.html")

def teacher_dash(request):
    return render(request, "teachers/teacher_dash.html")
# articles doesn't render article.html but article_page

def teacher_login(request):
    return render(request, "teachers/teacher_login.html")

def teacher_registration(request):
    return render(request, "teachers/teacher_registration.html")

def teachers(request):
    return render(request, "teachers/teacher_registration.html")