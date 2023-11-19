from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .EmailBackEnd import EmailBackEnd






def customerregistration(request):
 if request.method == 'POST':
  username = request.POST.get('username')
  email = request.POST.get('email')
  password = request.POST.get('password')

  if CustomUser.objects.filter(username=username).exists():
    messages.warning(request, 'Username is already taken')

  if CustomUser.objects.filter(email=email).exists():
    messages.warning(request, 'Email is already taken')

  else:
    user = CustomUser(username=username, email=email)
    user.set_password(password)
    user.user_type=2
    user.save()

    messages.success(request, 'Congratulation..! You are registered Successfully')
  

 return render(request, 'register.html')



def loginuser(request):
 if request.method == 'POST':
        user = EmailBackEnd.authenticate(request, username=request.POST.get('email'), password=request.POST.get('password'),)
        if user:
            #user is authenticated
            login(request, user)
            user_type = user.user_type
            if user_type == '1':
                return redirect('Pharma')
            elif user_type == '2':
                return redirect('/')
            
 return render(request, 'login.html')




def logoutuser(request):
  logout(request)
  return redirect('/')