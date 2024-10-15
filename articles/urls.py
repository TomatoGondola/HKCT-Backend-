from django.urls import path
from . import views

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>', views.articles, name='article'),
    path('article_page', views.article_page, name='article_page')
]