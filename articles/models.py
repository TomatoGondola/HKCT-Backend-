from django.db import models
from teachers.models import Teacher
from datetime import datetime

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    title = models.CharFIeld(max_length=200)
    author_date = models.DateTimeField(default=datetime.now, blank=True)
    para_1 = models.TextField(max_length=450)
    para_2 = models.TextField(max_length=450)
    para_3 = models.TextField(max_length=450)
    quote = models.CharField(max_length=125)
    note = models.TextField(max_length=100)
    source = models.TextField(max_length=100)
    photo_head = models.ImageField(upload_to='articles_photos/%Y/%m/%d')
    photo_body = models.ImageField(upload_to='articles_photos/%Y/%m/%d', blank=True)
    photo_footer = models.ImageField(upload_to='articles_photos/%Y/%m/%d', blank=True)
    
    def __str__(self):
        return self.title