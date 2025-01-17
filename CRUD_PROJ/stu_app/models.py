from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    age = models.FloatField()
    marks = models.FloatField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.roll} --- {self.name} "


class Subject(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    sub = models.CharField(max_length=20)