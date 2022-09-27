from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from attendance.settings import LOGIN_URL
# Create your views here.

@login_required(login_url='/login')
def hodash(request):
    return render(request,'hod.html')

@login_required(login_url=LOGIN_URL)
def create_faculty(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email =request.POST.get('email')
        #Add Code To send mail
        return redirect('create_faculty')
    return render(request,'create_faculty.html')