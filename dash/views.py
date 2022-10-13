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
    if request.method == "POST":
        sem = request.POST.get('sem')
        year = request.POST.get('year')
        section = request.POST.get('section')
        staff = request.POST.get('staff')
        dat1 = faculty_detail.objects.get(name=staff)
        db_ins = classes(
            sem=sem,
            year=year,
            section=section,
            teacher=dat1
        )
        db_ins.save()
        messages.success(request,"Class Created!!")
        return redirect('create_class')

    dat = faculty_detail.objects.all()
    cont={'staffs':dat}
    return render(request,'create_class.html',context=cont)

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['hod'])
def assign_subject(request):
    if request.method == 'POST':
        sub_code= request.POST.get('subject_code')
        staff = request.POST.get('staff')
        classs = request.POST.get('clas')
        db_inst = subject(
            subject_code= course.objects.get(c_id=sub_code),
            staff_id=faculty_detail.objects.get(email=staff),
            class_id=classes.objects.get(class_id=classs)
        )
        db_inst.save()
        messages.success(request,'Class Created!!')
        return redirect('assign_subject')

    subj =course.objects.all()
    staf =faculty_detail.objects.all()
    clas = classes.objects.all()
    context ={'subjects':subj,'staffs':staf,'classes':clas}
    return render(request,'assign_subject.html',context=context)


@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def facdash(request):
    return render(request, 'facdash.html')

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def add_students(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        roll_no = request.POST.get('roll_no')
        register_no = request.POST.get('register_no')
        clas = request.POST.get('clas')

        db_inst = student_detail(
            name=name,
            email=email,
            roll_no=roll_no,
            reg_no=register_no,
            s_class=classes.objects.get(class_id=clas)
        )
        db_inst.save()
        messages.success(request, 'Student Added!!')
        return redirect('add_students')
    clas = classes.objects.all()
    context ={'classes':clas}
    return render(request, 'add_students.html',context)

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def list_students(request):
    students = student_detail.objects.all()
    cont={'students': students}
    return render(request, 'list_students.html', context=cont)


@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def mark_attendance(request):
    students = student_detail.objects.all()
    cont={'students': students}
    return render(request, 'mark_attendance.html', context=cont)

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def add_timetable(request):
    email=request.session['staff_email']
    subj = subject.objects.filter(staff_id=email)
    context = {'subjects':subj}
    return render(request, 'add_timetable.html', context=context)
