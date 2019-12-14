from django.db import models

# Create your models here.

class Mistor(models.Model):
  name = models.CharField(max_length=120)
  ip = models.CharField(max_length=120)

class CalcHistory(models.Model):
  date = models.DateTimeField()
  first = models.IntegerField()
  second = models.IntegerField()
  result = models.IntegerField()
  author = models.ForeignKey(to=Mistor, null=True, on_delete=models.SET_NULL)
