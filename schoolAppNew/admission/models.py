from django.db import models
from django.urls import reverse

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length = 1000)
    fathername = models.CharField(max_length = 1000)
    classname = models.IntegerField()
    contact = models.CharField(max_length = 1000)

class Teacher(models.Model):
    name = models.CharField(max_length = 1000)
    subject = models.CharField(max_length = 1000)
    experience = models.IntegerField()
    contact = models.CharField(max_length = 1000)
    def get_absolute_url(self):
        return reverse('listteachers')
