from re import sub
from time import time
from django.contrib import admin
from .models import faculty_detail, classes, student_detail, attendance, subject, course, timetable

# Register your models here.
admin.site.register(faculty_detail)
admin.site.register(classes)
admin.site.register(student_detail)
admin.site.register(attendance)
admin.site.register(subject)
admin.site.register(course)
admin.site.register(timetable)