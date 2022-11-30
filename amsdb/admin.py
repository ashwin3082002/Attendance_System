from re import sub
from time import time
from django.contrib import admin
from .models import faculty_detail, classes, student_detail, attendance, subject, course, timetable, stu_atten

# Register your models here.
from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']

admin.site.register(Session, SessionAdmin)
admin.site.register(faculty_detail)
admin.site.register(classes)
admin.site.register(student_detail)
admin.site.register(attendance)
admin.site.register(subject)
admin.site.register(course)
admin.site.register(timetable)
admin.site.register(stu_atten)