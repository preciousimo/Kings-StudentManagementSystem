from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.contrib import messages
from student_management_app.models import CustomUser

# Create your views here.
def loginPage(request):
    return render (request, 'login.html')

def registerPage(request):
    return render (request, 'register.html')

def registerUser(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        second_name = request.POST['second_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        user = CustomUser.objects.create_user(first_name=first_name,second_name=second_name,email=email,password=password,password2=password2, user_type=1)
        user.save()      
        messages.success(request, first_name,' created successfully')  
        return HttpResponseRedirect('admin_home')
    else:
        return HttpResponse('<h2>Method not allowed</h2>')
        return HttpResponseRedirect('register')
    
def logoutUser(request):
    logout(request, user)
