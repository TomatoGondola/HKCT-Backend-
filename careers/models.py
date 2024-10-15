from django.db import models
from courses.models import Courses
from datetime import datetime


# Create your models here.

class Career(models.Model):
    course = models.ForeignKey('Course', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    flavor_text = models.CharField(max_length=75)
    company = models.CharField(max_length=200)
    company_desc = models.TextField(max_length=400)
    description = models.TextField(max_length=200)
    address = models.CharField(max_length=200)
    special = models.CharField(max_length=100)
    work_type = models.CharField(max_length=100)
    wages = models.IntegerField()
    location = models.CharField(max_length=75)
    link = models.CharField(max_length=100)
    list_date = models.DateTimeField(auto_now_add=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    photo_icon = models.ImageField(upload_to='photos/%Y/%m/%d') 
    
    def __str__(self):
        return self.title