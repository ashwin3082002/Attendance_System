from django.db import models

# Create your models here.
class faculty_details(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=120)
