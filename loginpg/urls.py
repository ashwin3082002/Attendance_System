from django.urls import path
from . import views

urlpatterns = [
    path('',views.ulogin, name="ulogin"),
]