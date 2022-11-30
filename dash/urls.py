from django.urls import path
from . import views

urlpatterns = [
    path('hod',views.hodash, name='hodash'),
    path('hod/create-faculty', views.create_faculty, name="create_faculty"),
    path('hod/create-faculty1', views.create_faculty1, name="create_faculty1"),
    path('hod/create-course', views.create_course, name="create_course"),
    path('hod/create-class', views.create_class, name="create_class"),
    path('hod/assign_subject', views.assign_subject, name="assign_subject"),
    path('hod/assign_class', views.create_course, name="assign_class"),

    path('faculty',views.facdash, name='facdash'),
    path('faculty/add-students', views.add_students,name="add_students"),
    path('faculty/list-students', views.list_students,name="list_students"),
    path('faculty/list-students', views.list_students,name="list_students"),
    path('faculty/attendance', views.mark_attendance,name="mark_attendance"),
    path('faculty/timtable', views.add_timetable, name="add_timetable"),
    path('faculty/showreport', views.showreport, name="showreport"),
    path('sendwarning', views.sendwarning,name="sendwarning"),
]
