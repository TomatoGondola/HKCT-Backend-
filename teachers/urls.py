from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_registration, name='teacher_registration'),
    path('<int:teacher_id>', views.teachers, name='teacher'),
    path('teacher_dash', views.teacher_dash, name='teacher_dash'),
    path('teacher_login', views.teacher_login, name='teacher_login')
]