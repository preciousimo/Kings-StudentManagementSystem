from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from student_management_app.models import CustomUser
from django.shortcuts import render
from django.contrib import messages


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
        user = CustomUser.objects.create_user(first_name=first_name,second_name=second_name,email=email,password=password,user_type=1)
        user.save()        
        return HttpResponseRedirect('admin_home')
    
def logoutUser(request):
    logout(request, user)
