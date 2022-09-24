from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def ulogin(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username=username, password=password)
        if user is not None:
                login(request,user)
                return redirect('hodash')
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('ulogin')
    return render(request,'login.html')