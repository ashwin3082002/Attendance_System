from django.urls import path
from . import views

urlpatterns = [
    path('hod',views.hodash, name='hodash'),
    path('hod/create-faculty', views.create_faculty, name="create_faculty"),
    path('faculty',views.facdash, name='facdash')
]
