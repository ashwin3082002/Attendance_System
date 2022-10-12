from django.urls import path
from . import views

urlpatterns = [
    path('hod',views.hodash, name='hodash'),
    path('hod/create-faculty', views.create_faculty, name="create_faculty"),
    path('hod/create-course', views.create_course, name="create_course"),
    path('hod/create-class', views.create_class, name="create_class"),
    path('hod/assign_subject', views.create_course, name="assign_subject"),
    path('hod/assign_class', views.create_course, name="assign_class"),

    path('faculty',views.facdash, name='facdash')
]
