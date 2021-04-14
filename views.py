from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import employee
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
import random

def register(request):
    if request.method=="POST":
        emp_name=request.POST['name']
        emp_email=request.POST['email']
        emp_mobile=request.POST['mobile']
        emp_address=request.POST['address']
        emp_state=request.POST['state']
       
        employee.objects.create(name=emp_name,email=emp_email,mobile=emp_mobile,address=emp_address,state=emp_state)
        messages.success(request,"Registeration successfull")
        return redirect('register')
        #return HttpResponse("Registration Successfully!")
    return render(request,'register.html')   


def all_data(request):
    data=employee.objects.all()
    return render(request,'alldata.html',{'data': data})

def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        is_auth=authenticate(username=username,password=password)
        if is_auth is None:
            messages.warning(request,"Invalid Credentials")
            return redirect('login')
        else: 
            login(request,is_auth)
            messages.success(request,"logged in successfully")
            return redirect('alldata')
    return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('login')
   

# def forgot_password(request):
#     if request.method == "POST":
#         email = request.POST['email']
#         user_data = User.objects.get(email=email)
#         personal = Personal.objects.get(user=user_data)
#         otp = random.randint(1000,100000)
#         personal.otp = otp
#         personal.save()
#         send_mail('Forgot Password','Please use following otp for updating the password '+str(otp),settings.EMAIL_HOST_USER,[user_data.email])
#         return redirect('update_pwd',personal.id)
#     return render(request,'forgot_pwd.html')

# def update_password(request,id):
#     if request.method == "POST":
#         otp = request.POST['otp']
#         password = request.POST['password']
#         personal = Personal.objects.get(id=id)
#         if personal.otp == otp:
#             user_data = User.objects.get(email=personal.user.email)
#             user_data.set_password(password)
#             user_data.save()
#             return HttpResponse("Password updated")
#         else:
#             return HttpResponse("Incorrect OTP!")
#     return render(request,'update_pwd.html')   