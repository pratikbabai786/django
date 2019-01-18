from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=30)
    no=models.IntegerField()
    marks=models.FloatField()

class Employee(models.Model):
    name=models.CharField(max_length=30)
    no=models.IntegerField()
    sal=models.FloatField()
