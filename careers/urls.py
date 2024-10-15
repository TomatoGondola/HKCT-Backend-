from django.urls import path
from . import views

urlpatterns = [
    path('', views.careers, name='careers'),
    path('<int:career_id>', views.careers, name='career'),
    path('career_page', views.career_page, name='career_page')
]