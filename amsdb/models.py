from datetime import date
from random import choices
from django.db import models

# Create your models here.
class faculty_detail(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(primary_key=True)

    def __str__(self):
        return self.name

class classes(models.Model):
    class_id = models.AutoField(primary_key=True)
    sem = models.CharField(max_length=120)
    year = models.CharField(max_length=120)
    section = models.CharField(max_length=120)
    teacher = models.ForeignKey(faculty_detail, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.year} Year, {self.section} Section'

class student_detail(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    roll_no = models.CharField(max_length=120, primary_key=True)
    reg_no = models.CharField(max_length=120)
    s_class = models.ForeignKey(classes,on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_no

class course(models.Model):
    c_name = models.CharField(max_length=120)
    c_id = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.c_name

class subject(models.Model):
    sub_id = models.AutoField(primary_key=True)
    subject_code = models.ForeignKey(course,on_delete=models.CASCADE)
    staff_id = models.ForeignKey(faculty_detail,on_delete=models.CASCADE)
    class_id = models.ForeignKey(classes,on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_code.c_name

class attendance(models.Model):
    roll_no = models.ForeignKey(student_detail,on_delete=models.CASCADE)
    s_class = models.ForeignKey(classes,on_delete=models.CASCADE)
    overall = models.CharField(max_length=120)
    first = models.CharField(max_length=120)
    second = models.CharField(max_length=120)
    third = models.CharField(max_length=120)
    fourth = models.CharField(max_length=120)
    fifth = models.CharField(max_length=120)
    sixth = models.CharField(max_length=120)
    seveen = models.CharField(max_length=120)
    eight = models.CharField(max_length=120)
    date = models.DateField()

    def __str__(self):
        return f"{self.roll_no} - {self.date}"

class timetable(models.Model):
    class_s = models.ForeignKey(classes, on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    first = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='First_Hour')
    second = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='Second_Hour')
    third = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='Third_Hour')
    fourth = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='Fourth_Hour')
    fifth = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='Fifth_Hour')
    sixth = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='Sixth_Hour')
    seveen = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='Seveen_Hour')
    eight = models.ForeignKey(subject,on_delete=models.CASCADE, related_name='Eight_Hour')