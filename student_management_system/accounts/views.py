from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from student_management_app.models import CustomUser
from django.contrib import messages
from student_management_app import urls
from student_management_app.EmailBackEnd import EmailBackEnd
from django.http import HttpResponse
from student_management_app.models import CustomUser
# Create your views here.
   
def registerPage(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            '''
            if EmailBackEnd.objects.filter(username=username).exists():
                messages.info(request, '{} already taken'.format(username))
                return render(request, 'register.html')
            elif EmailBackEnd.objects.filter(email=email).exists():
                messages.info(request, '{} already taken'.format(email))
                return render(request, 'register.html')
            else:
                '''
            try:
                user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password, user_type=1)
                user.save() 
                messages.success(request,'{} created successfully'.format(username)) 
                return redirect('/login')
            except:
                messages.error(request,'Invalid Credentials') 
                return render(request, 'register.html')
        else:
            messages.error(request,'Passwords do not match') 
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = EmailBackEnd.authenticate(request, username=username,password=password)
        if user != None:
            login(request, user)
            if user.user_type == "1" :
                return redirect('/admin-home')
            elif user.user_type == "2" :
                return redirect('/staff-home')
            elif user.user_type == "3" :
                return redirect('/student-home')
            else:
                return HttpResponse('Invalid User')
        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    messages.info(request, 'Logged out Successfully')
    return redirect('/login')