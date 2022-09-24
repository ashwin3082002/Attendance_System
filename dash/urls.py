
from django.urls import path
from . import views

urlpatterns = [
    path('hod',views.hodash, name='hodash')
]
