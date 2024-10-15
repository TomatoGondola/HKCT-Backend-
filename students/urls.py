from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_login, name='student_login'),
    path('<int:student_id>', views.students, name='student'),
    path('student_dash', views.student_dash, name='student_dash'),
    path('student_login', views.student_login, name='student_login')
]