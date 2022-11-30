from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from attendance.settings import LOGIN_URL
from django.contrib.auth.models import User
from amsdb.models import faculty_detail, classes, student_detail, attendance, subject, course, timetable,stu_atten
from django.contrib import messages
from django.contrib.auth.models import Group
from util import func
from .decoraters import allowed_users
import datetime
import random

# Create your views here.

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['hod'])
def hodash(request):
    stu = student_detail.objects.all()
    cont = {'count':len(stu)}
    return render(request,'hod.html',context=cont)

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['hod'])
def create_faculty(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email =request.POST.get('email')
        password = User.objects.make_random_password()
        db_instance = faculty_detail(
            name=name,
            email=email,
            class_teacher = True
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
def create_faculty1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email =request.POST.get('email')
        db_instance = faculty_detail(
            name=name,
            email=email,
            class_teacher = False
        )
        db_instance.save()
        messages.error(request, "Faculty Created!!!")
        return redirect('create_faculty1')

    return render(request,'create_faculty1.html')

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

    dat = faculty_detail.objects.filter(class_teacher=True)
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
        messages.success(request,'Subject Created!!')
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
    email=request.session['staff_email']
    fac = faculty_detail.objects.get(email=email)
    clas = classes.objects.get(teacher=fac)
    students = student_detail.objects.all()
    currentdate = datetime.date.today()
    day = currentdate.strftime("%A")
    tt = timetable.objects.get(day=day)


    if request.method == "POST":
        cn = 1
        for i in request.POST:
            if cn==1:
                cn+=1
                continue
            stu=student_detail.objects.get(roll_no=i)
            class_id = stu.s_class.class_id
            clas = classes.objects.get(class_id=class_id)
            data=request.POST.getlist(i)
            dic = {
                'overall':data[0],
                'first':data[1],
                'second':data[2],
                'third':data[3],
                'fourth':data[4],
                'fifth':data[5],
                'sixth':data[6],
                'seveen':data[7],
                'eight':data[8],
            }
            if dic['overall'] == "a":
                dic['first'] = "a"
                dic['second'] = "a"
                dic['third'] = "a"
                dic['fourth'] = "a"
                dic['fifth'] = "a"
                dic['sixth'] = "a"
                dic['seveen'] = "a"
                dic['eight'] = "a"

            db_ins = attendance(
                roll_no = stu,
                s_class = clas,
                overall = dic['overall'],
                first = dic['first'],
                second = dic['second'],
                third = dic['third'],
                fourth = dic['fourth'],
                fifth = dic['fifth'],
                sixth = dic['sixth'],
                seveen = dic['seveen'],
                eight = dic['eight'],
                date= datetime.date.today()
            )
            db_ins.save()
        messages.success(request,"Attendance Marked!!")

        return redirect('mark_attendance')


    cont={'students': students,'tt':tt,'classs':clas,'range':range(9)}
    return render(request, 'mark_attendance.html', context=cont)

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def add_timetable(request):
    email=request.session['staff_email']

    fac = faculty_detail.objects.get(email=email)
    try:
        clas = classes.objects.get(teacher=fac)
    except:
        messages.error(request,'You have not been assigned a Class!! Kindly contact HOD')
        return redirect('facdash')
    

    if request.method == 'POST':
        m1 = request.POST.get('m1')
        m2 = request.POST.get('m2')
        m3 = request.POST.get('m3')
        m4 = request.POST.get('m4')
        m5 = request.POST.get('m5')
        m6 = request.POST.get('m6')
        m7 = request.POST.get('m7')
        m8 = request.POST.get('m8')
        t1 = request.POST.get('t1')
        t2 = request.POST.get('t2')
        t3 = request.POST.get('t3')
        t4 = request.POST.get('t4')
        t5 = request.POST.get('t5')
        t6 = request.POST.get('t6')
        t7 = request.POST.get('t7')
        t8 = request.POST.get('t8')
        w1 = request.POST.get('w1')
        w2 = request.POST.get('w2')
        w3 = request.POST.get('w3')
        w4 = request.POST.get('w4')
        w5 = request.POST.get('w5')
        w6 = request.POST.get('w6')
        w7 = request.POST.get('w7')
        w8 = request.POST.get('w8')
        th1 = request.POST.get('th1')
        th2 = request.POST.get('th2')
        th3 = request.POST.get('th3')
        th4 = request.POST.get('th4')
        th5 = request.POST.get('th5')
        th6 = request.POST.get('th6')
        th7 = request.POST.get('th7')
        th8 = request.POST.get('th8')
        f1 = request.POST.get('f1')
        f2 = request.POST.get('f2')
        f3 = request.POST.get('f3')
        f4 = request.POST.get('f4')
        f5 = request.POST.get('f5')
        f6 = request.POST.get('f6')
        f7 = request.POST.get('f7')
        f8 = request.POST.get('f8')
        dic = {'Monday':[m1,m2,m3,m4,m5,m6,m7,m8],'Tuesday':[t1,t2,t3,t4,t5,t6,t7,t8],'Wednesday':[w1,w2,w3,w4,w5,w6,w7,w8],'Thursday':[th1,th2,th3,th4,th5,th6,th7,th8],'Friday':[f1,f2,f3,f4,f5,f6,f7,f8]}
        for i in dic:
            db_inst = timetable(
                class_s = clas,
                day = i,
                first= subject.objects.get(sub_id=dic[i][0]),
                second= subject.objects.get(sub_id=dic[i][1]),
                third= subject.objects.get(sub_id=dic[i][2]),
                fourth= subject.objects.get(sub_id=dic[i][3]),
                fifth= subject.objects.get(sub_id=dic[i][4]),
                sixth= subject.objects.get(sub_id=dic[i][5]),
                seveen= subject.objects.get(sub_id=dic[i][6]),
                eight= subject.objects.get(sub_id=dic[i][7])
            )
            db_inst.save()
        messages.success(request,"Timetable Added")
        return redirect('facdash')
    
    email=request.session['staff_email']
    clas = classes.objects.get(teacher=fac)
    subj = subject.objects.filter(class_id=clas.class_id)
    context = {'subjects':subj}
    return render(request, 'add_timetable.html', context=context)

@login_required(login_url=LOGIN_URL)
@allowed_users(allowed_roles=['faculty'])
def showreport(request):
    stu_atten.objects.all().delete()
    email=request.session['staff_email']
    fac = faculty_detail.objects.get(email=email)
    clas = classes.objects.get(teacher=fac)
    students = student_detail.objects.filter(s_class = clas)
    attendanc = attendance.objects.filter(s_class = clas)
    stu =  list(student_detail.objects.all())
    ran_stu = random.choice(stu)
    atten = attendance.objects.filter(roll_no = ran_stu)
    working_days = len(list(atten))
    if working_days==0:
        working_days=1
    stu1=student_detail.objects.all()

    for i in stu1: 
        present = len(list(attendance.objects.filter(roll_no=i,overall="p")))
        absent = len(list(attendance.objects.filter(roll_no=i,overall="a")))
        percentage = (present/working_days)*100
        status=""
        if percentage>75:
            status=False
        else:
            status=True    
        db_inst = stu_atten(
            name=i.name,
            roll = i.roll_no,
            total_present = present,
            total_absent = absent,
            percentage = percentage,
            status=status,
            date_gen = datetime.date.today()
        )
        db_inst.save()
    stu_det = stu_atten.objects.filter(date_gen=datetime.date.today())
    
        
    
    context = {"students":stu_det, "working_days":working_days}
    
    return render(request, 'showreport.html', context=context)

def sendwarning(request):
    if request.method == "POST":
        roll = request.POST.get("roll")
        stu = student_detail.objects.get(roll_no=roll)
        if func.send_warning_mail(stu.email,stu.name):
            messages.success(request, "Warning Sent!!")
        else:
            messages.success(request,"Warning not Sent!!")
    return redirect("showreport")