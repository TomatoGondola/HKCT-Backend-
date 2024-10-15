from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:course_id>', views.courses, name='course'),
    path('course_page', views.course_page, name='course_page')
]