from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
# Create your views here.


def show_auth_page(request):
    if request.user.is_authenticated:  
        return redirect('/')
    return render(request,'auth.html')



def show_profile_page(request):
    user=request.user
    context={
        'user':user
    }
    return render(request,'profile.html',context)


def login_view(request):
    username=request.POST.get('loginName')
    password=request.POST.get('loginPassword')
    user=authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect('/')
    messages.error(request,'Login failed')
    return redirect('accounts:show_auth_page')

def signup_view(request):
    username=request.POST.get('username')
    password1=request.POST.get('password1')
    password2=request.POST.get('password2')
    email=request.POST.get('email')
    name=request.POST.get('name')
    if (password1 == password2) and username and email:
        if (User.objects.filter(username=username).exists):
            messages.error(request,"user name is already exists")
        else:   
            
            user=User.objects.create(username=username,name=name,password=password1,email=email)
            if user:
                login(request,user)
            else:
                messages.error(request,'SignUp failed')
    else:
        messages.error(request,'check your entered a valid user name or password1 = password2')

    return redirect('/')



def logout_view(request):
    logout(request)
    return redirect('/')


def update_profile(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    image=request.FILES.get('image')
   
    try:
        user=request.user
        user.name=name
        user.email=email
        user.image=image
        user.save()
        messages.success(request,"profile update successfully")
        return redirect('/')
    except IntegrityError:
        messages.error(request,'email already exist')
    return redirect("accounts:show_profile_page")
