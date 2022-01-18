from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.auth.contrib import login, logout, authenticate
from django.shortcuts import render

from student_management_app.EmailBackEnd import EmailBackEnd

# Create your views here.
def homePage(request):
    
    return render (request, 'home.html')

def loginPage(request):
    return render (request, 'login.html')

def loginUser(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request,request.POST.get('email'),request.POST.get('password'))
        if user != None:
            login(request, user)
            return HttpResponse("Email :"+request.POST.get('email')+ " Password:"+request.POST.get('password'))
        else: 
            return HttpResponse('Invalid Login')

def getUserDetails(request):
    if request.user!=None:
        return HttpResponse('User: '+request.user.email+ ' usertype : '+request.user.user_type)
    else:
        return HttpResponse('Please Login First')
        return HttpResponseRedirect('/')

