from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, auth
from django.contrib import messages
from student_management_app import urls

# Create your views here.
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/admin-home')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    

def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, '{} already taken'.format(username))
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, '{} already taken'.format(username))
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save() 
                messages.success(request, '{} created successfully'.format(username))   
                return redirect('/admin-home')  
        else:
            messages.error(request,'Passwords do not match')
            #messages.success(request, first_name,' created successfully')  
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logoutPage(request):
    auth.logout(request)
    return redirect('/login')