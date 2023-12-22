from django.contrib import messages
from django.contrib.auth import authenticate,login as authlogin,logout as authlogout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Form





# Create your views here.

def logout(request):
    authlogout(request)
    return redirect('/')
def log(request):
    if request.POST:
        username=request.POST['username']
        password = request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            authlogin(request, user)
            return redirect('/details')
        else:
            messages.info(request, "invalid username or password")
    return render(request, 'login.html')



def home(request):
    return render(request,'home.html')

def thrissur(request):
    return render(request,'thrissur.html')
def ernakulam(request):
    return render(request,'ernakulam.html')
def kollam(request):
    return render(request,'kollam.html')
def kottayam(request):
    return render(request,'kottayam.html')
def kannur(request):
    return render(request,'kannur.html')
def details(request):
    return render(request,'details.html')

def registers(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")

            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('log/')

        else:
            messages.info(request,"password not matching")
    return render(request,'register.html')


def details(request):

    return render(request, 'thrissur.html')



def dependantfield(request):

    return render(request, 'details.html')

