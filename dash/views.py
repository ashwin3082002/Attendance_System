from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from attendance.settings import LOGIN_URL
from django.contrib.auth.models import User
from amsdb.models import faculty_detail, classes, student_detail, attendance, subject, course, timetable
from django.contrib import messages
from django.contrib.auth.models import Group
from util import func
from .decoraters import allowed_users
# Create your views here.

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['hod'])
def hodash(request):
    return render(request,'hod.html')

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['hod'])
def create_faculty(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email =request.POST.get('email')
        password = User.objects.make_random_password()
        db_instance = faculty_detail(
            name=name,
            email=email
        )
        if func.faculty_creation_mail(email,password, name):
            db_instance.save()
            user = User.objects.create_user(email, email, password)
            user.first_name=name
            group = Group.objects.get(name='faculty')
            user.groups.add(group)
            user.save()
            messages.error(request, "Faculty Created!!!")
            return redirect('create_faculty')
            
        else:
            messages.error(request, "Something Went Wrong!!! Try Again...")
        return redirect('create_faculty')
    return render(request,'create_faculty.html')

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['hod'])
def create_course(request):
    if request.method=='POST':
        sub_id = request.POST.get('subject_id')
        sub_nam = request.POST.get('subject_name')
        db_ins = course(
            c_name=sub_nam,
            c_id = sub_id
        )
        db_ins.save()
        messages.success(request,'Course Added!!')
        return redirect('create_course')

    return render(request,'create_course.html')

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['hod'])
def create_class(request):
    return render(request,'create_class.html')


@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def facdash(request):
    return render(request, 'facdash.html')


