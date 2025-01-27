from django.shortcuts import render,redirect
from .models import Register1
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def About(request):
    return render(request,'AboutUs.html')
def Contact(request):
    return render(request,'ContactUs.html')
def Courses(request):
    return render(request,'Courses.html')
def Faculty(request):
    return render(request,'Faculty.html')
def Register(request):
    if request.method=="POST":
        username=request.POST['username']
        full_name=request.POST['full_name']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1!=password2:
            return render(request,"Register.html",{"error":'password must match'})
        elif User.objects.filter(username=username).exists():
            return render(request,"Register.html",{"error":'username already exits'})
        elif User.objects.filter(email=email).exists():
            return render(request,"Register.html",{"error":'email already exits'})
        else:
            user=User.objects.create_user(username=username,email=email,password=password1)
            user=Register1(full_name=full_name,mobile=mobile)
            user.save()
            messages.success(request,'saved successfully')
            return redirect('/index/')
    else:
        return render(request,"Register.html")
    
def Login(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password1']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/index/')
        else:
            messages.info(request,"INVALID USER OR PASSWORD")
            return redirect('/Login/')
    else:
        return render(request,"Login.html")
    
def Logout(request):
    auth.logout(request)
    return render(request,'index.html')

    