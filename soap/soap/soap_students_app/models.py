from django.db import models

# Create your models here.
class Student(models.Model):
    admission = models.PositiveIntegerField()
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    entry_points = models.PositiveIntegerField()
    reg_date = models.DateTimeField('registration date')
    def __str__(self):
        return self.full_name
