from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def loginPage(request):
    return render (request, 'login.html')

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
                messages.info(request, '{{username}} already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, '{{email}} already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save() 
                messages.success(request, '{{username}} created successfully')   
                return HttpResponseRedirect('student_management_app/admin-home')  
        else:
            messages.info(request,'Passwords do not match')
            #messages.success(request, first_name,' created successfully')  
            return redirect('register')
    else:
        return redirect('register')
        