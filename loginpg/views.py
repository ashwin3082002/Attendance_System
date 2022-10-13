from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from amsdb.models import faculty_detail

# Create your views here.

def ulogin(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username=username, password=password)
        try:
            b = list(user.groups.filter(name='faculty'))!=[]
        except:
            messages.error(request,"Incorrect Credentials")
            return redirect('ulogin')
        
        if b and user is not None:
            login(request,user)
            staff = faculty_detail.objects.get(email=username)
            request.session['staff_email']=staff.email
            return redirect('facdash')
        elif user is not None:
                login(request,user)
                return redirect('hodash')
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('ulogin')
    return render(request,'login.html')