import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from student_management_app.models import CustomUser
from django.contrib import messages
from student_management_app import urls
from student_management_app.EmailBackEnd import EmailBackEnd
from django.http import HttpResponse
from student_management_app.models import CustomUser
import requests
from django.views.decorators.csrf import csrf_exempt
from accounts.forms import RegisterAdminForm
# Create your views here.
   
def registerPage(request):
    form = RegisterAdminForm()
    return render(request, 'register.html', {'form':form})

def registerPageSave(request):
    if request.method == 'POST':
        form = RegisterAdminForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            if password == password2:
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
            form = RegisterAdminForm(request.POST)
            return render(request, 'register.html', {'form':form})
    else:
        return HttpResponse('Method not allowed')

@csrf_exempt
def checkAdminEmailExist(request):
    email = request.POST['email']
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def checkAdminUsernameExist(request):
    username = request.POST['username']
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        '''
        captcha_token = request.POST['g-recaptcha-response']
        cap_url = "https://www.google.com/recaptcha/api/siteverify"
        cap_secret = "6LePnE8fAAAAABF9gJ6mtafoML8b7EPTx51bvPBm"
        cap_data = {"secret":cap_secret, "response":captcha_token}
        cap_server_response = requests.post(url=cap_url,data=cap_data)
        cap_json = json.loads(cap_server_response.text)
        
        if cap_json['success'] == False:
            messages.error(request, 'Invalid Captcha Try Again')
            return render(request, 'login.html')
        '''
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

