from django.db import models
from datetime import datetime

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    list_date = models.DateTimeField(auto_now_add=True)
    edu_require = models.TextField(blank=True)
    hierarchy =  models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    seats = models.IntegerField()
    
    def __str__(self):
        return self.title
    