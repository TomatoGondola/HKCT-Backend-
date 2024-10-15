from django.urls import path
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('<int:thread_id>', views.thread, name='thread'),
    path('thread', views.thread, name='thread'),
    path('forum_thread', views.forum_thread, name='forum_thread')
]