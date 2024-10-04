
from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import *
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseBadRequest





def index(request):
    return render(request, 'index.html')

def mainpage(request):
    
    if request.method == 'POST' and 'stdinfo' in request.POST:
        hall_ticket_number = request.POST.get('hallticketnumber')
        student_name = request.POST.get('name')
        father_name = request.POST.get('fathername')
        mother_name = request.POST.get('mothername')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        zincode = request.POST.get('code')
        qualification = request.POST.get('qualification')
        year_of_passout = request.POST.get('YOP')
        course_duration = request.POST.get('course')
        enroll_date = request.POST.get('enrollingdate')
        mobile = request.POST.get('mobilenum')
        emergency_num = request.POST.get('emergencynum')
        print(hall_ticket_number,student_name,gender,email,year_of_passout)
        if hall_ticket_number and student_name and gender and email:
            print(hall_ticket_number,student_name,gender,email)
            Student.objects.create(
                HallTickectnumber=hall_ticket_number,
                Student_name=student_name,
                Father_name=father_name,
                Mother_name=mother_name,
                Email=email,
                Gender=gender,
                Address=address,
                Zincode=zincode,
                Qualification=qualification,
                Yearofpassout=str(year_of_passout),
                Enroll_date=enroll_date,
                Course_duration=course_duration,
                Moblie=mobile,
                Emergengynum=emergency_num,
            ).save()
    if request.method == 'POST' and 'staffinfo' in request.POST:
        Name = request.POST.get('staffname')
        emailid = request.POST.get('Staffemail1')
        password = request.POST.get('staffpassword')
        age = request.POST.get('staffage')
        address = request.POST.get('staffaddress')
        position = request.POST.get('position')
        employment_type = request.POST.get('employment_type')
        joining_date = request.POST.get('joining_date')
        employee_id = request.POST.get('employee-id')
        qualifications = request.POST.get('qualifications')
        institution = request.POST.get('institution')
        graduation_year = request.POST.get('graduation_year')

        print(Name,emailid,password,age,address)
        if Name and emailid and password and age and address:
            print(Name,emailid,password,age,address)
            staff1.objects.create(
                name=str(Name),
                emailid=emailid,
                password=password,
                age=age,
                Address=address,
                Position=position,
                Employment=employment_type,
                Dateofjoining=joining_date,
                Employmentid=employee_id,
                Highestqualification=qualifications,
                Institution=institution,
                Yearofgraduation=graduation_year,
                  ).save()
    if request.method == 'POST' and 'courseinfo' in request.POST:
             name = request.POST.get('name')
             fathername = request.POST.get('fathername')
             mothername = request.POST.get('mothername')
             email = request.POST.get('email')
             gender = request.POST.get('gender')
             name_course = request.POST.get('nameofcourses')
             specialization = request.POST.get('specialization')
             coursecode = request.POST.get('coursecode')
             course_duration = request.POST.get('courseduration')
             print(name,fathername,mothername, email,gender,name_course,specialization,coursecode,course_duration)
             if name and fathername and mothername and email and gender and name_course  and specialization:
                 Course.objects.create(
                     name = name,
                     fathername = fathername,
                     mothername = mothername,
                     email = email,
                     gender = gender,
                     name_course = name_course,
                     specialization = specialization,
                     coursecode = coursecode,
                     course_duration = course_duration
                     

                 ).save()
            
    data1=Student.objects.all()
    data2=staff1.objects.all()
    data3=Course.objects.all()
    for c in data3:
        print(c)
    context={
            'data1':data1,
            'data2':data2,
            'data3':data3,


    }
    
    
    return render(request, 'mainpage.html',context)

# def Login(request):
#     if request.method == "POST": 
#         username = request.POST['username']
#         password = request.POST['password']
#         user = auth.authenticate(username=username,password=password)
        
#         if user is not None:
#             auth.login(request, user)
#             return redirect('index.html')   
#         return render(request,'login.html')


def Login(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('mainpage')  # Redirect to the name of the URL pattern or view name
        else:
            # If authentication fails, return to login page with an error message
            return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')

def AdminLogin(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('index')  # Redirect to the name of the URL pattern or view name
        else:
            # If authentication fails, return to login page with an error message
            return render(request, 'AdminLogin.html', {'error': 'Invalid username or password'})

    return render(request, 'AdminLogin.html')

def Logout(request):
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('Login')  # Redirect to the name of the URL pattern or view name
        else:
            # If authentication fails, return to login page with an error message
            return render(request, 'Loginout.html', {'error': 'Invalid username or password'})

    return render(request, 'Logout.html')

def Studentform(request):
    return render(request, 'Studentform.html')