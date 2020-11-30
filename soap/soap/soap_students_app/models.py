from django.db import models

# Create your models here.
class Student(models.Model):
    admission = models.PositiveIntegerField()
    full_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_number = models.PositiveIntegerField()
    address = models.CharField(max_length=200)
    entry_points = models.PositiveIntegerField()
    reg_date = models.DateTimeField('registration date')
