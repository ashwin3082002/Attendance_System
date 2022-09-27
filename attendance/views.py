from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .settings import LOGIN_URL

# Create your views here.
def index(request):
    return render(request, 'index.html')

@login_required(login_url=LOGIN_URL)
def ulogout(request):
    logout(request)
    messages.success(request,'Logged Out!!')
    return redirect('home')