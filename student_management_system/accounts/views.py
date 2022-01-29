from django.shortcuts import render
from django.contrib.auth.models import User, auth
from student_management_app import EmailBackEnd
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
                return HttpResponse('Username taken')
            elif User.objects.filter(email=email).exists():
                return HttpResponse('Email taken')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                user.save() 
                return HttpResponse(username,' created successfully')   
                return HttpResponseRedirect('student_management_app/admin-home')  
        else:
            return HttpResponse('Passwords do not match')
            #messages.success(request, first_name,' created successfully')  
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')
        