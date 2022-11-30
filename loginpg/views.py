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
        
        if user is not None:
            try:
                role = str(user.groups.filter().get())
            except:
                messages.error(request, "Something Went Wrong!")
                return redirect('ulogin')
            if role == 'hod':
                login(request, user)
                return redirect('hodash')
            elif role == 'faculty':
                login(request, user)
                request.session['staff_email'] = request.user.username
                return redirect('facdash')
        else:
            messages.error(request, "Incorrect Credentials")
            return redirect('ulogin')

    return render(request,'login.html')