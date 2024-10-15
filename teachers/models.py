from django.db import models
from articles.models import Article
from courses.models import Course
from students.models import Student

# Create your models here.

class Teacher(models.Model):
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    assignment_1 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    homework_1 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    assignment_2 = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    course_mat = models.FileField(upload_to='files/%Y/%m/%d', blank=True)
    portrait = models.ImageField(upload_to='photo/%Y/%m/%d/')
    certified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    