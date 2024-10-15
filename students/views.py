from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "students/student_login.html")

def student_dash(request):
    return render(request, "students/student_dash.html")
# articles doesn't render article.html but article_page

def student_login(request):
    return render(request, "students/student_login.html")

def students(request):
    return render(request, "students/students.html")
