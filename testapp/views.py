from django.shortcuts import render,redirect
from .forms import UserRegistration
from django.http import HttpResponse
from .models import Users,User_profile,destination
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    error=None
    form=UserRegistration()
    if request.method=="POST":
        form=UserRegistration(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('Username')
            password=form.cleaned_data.get('Password')
            confirm_password=form.cleaned_data.get('Confirm_password')
            print(username)
            print(password)
            print(confirm_password)
            if password == confirm_password: 
                
                user = Users(Username=username, Password=password)
                user.save()
                print('user is saved',user)
                my_user=User_profile(my_username=username,my_password=password,f_username=user)
                my_user.save()
                my_users=User_profile.objects.all()
                # for item in my_users:
                #     d_user=destination.objects.create(
                #         d_username=item.my_username,
                #         d_password=item.my_password,
                #         d_foreignkey=item.f_username
                #     )
                #     d_user.save()
                print('my_user is saved',my_user)            
                return redirect('login')
            else:
                error='password doenst match'
               
    context={
        'form':form,
        'error':error
            }
    
    return render(request,'signup.html',context)

def login(request):
    error=None
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)
        
        try:
            user=Users.objects.get(Username=username)
            if user.Password==password:
                return redirect('welcome')
            else:
                error='incorrect password'
        except Users.DoesNotExist:
            error='user not registered ,please register'       
             
    return render(request,'login.html',{'error':error})

def welcome(request):
    return render(request,'welcome.html',)