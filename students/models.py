from django.db import models
from teachers.models import Teacher
from courses.models import Course

# Create your models here.

class Student(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)