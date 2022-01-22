from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib import messages
from student_management_app.EmailBackEnd import EmailBackEnd
from student_management_app import HodViews
from student_management_app.models import CustomUser

# Create your views here.
def homePage(request):
    return render (request, 'home.html')

def loginPage(request):
    return render (request, 'login.html')

def registerPage(request):
    return render (request, 'register.html')

def registerUser(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method not allowed</h2>')
        return HttpResponseRedirect('register')
    else:
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        user = CustomUser.objects.create_user(first_name=first_name,second_name=second_name,email=email,password=password,password2=password2,user_type=2)
        if user is True:
            user.save()
        else:
            return HttpResponse('Registration Successful')

def logoutUser(request):
    logout(request, user)
