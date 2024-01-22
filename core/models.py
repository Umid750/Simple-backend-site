from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 255)
    surname = models.CharField(max_length = 255)
    age = models.IntegerField()
    grade = models.IntegerField()
    birthday = models.DateField(auto_now = True)
    def __str__(self):
        return self.name