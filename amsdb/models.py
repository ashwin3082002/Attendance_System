from django.db import models

# Create your models here.
class faculty_detail(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return self.name

class student_detail(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    roll_no = models.CharField(max_length=120, primary_key=True)
    year = models.CharField(max_length=120)
    sem = models.CharField(max_length=120)
    section = models.CharField(max_length=100)

    def __str__(self):
        return self.roll_no

class course(models.Model):
    c_name = models.CharField(max_length=120)
    c_id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.c_name

class attendance(models.Model):
    roll_no = models.ForeignKey(student_detail,on_delete=models.CASCADE)
    status = models.CharField(max_length=120)