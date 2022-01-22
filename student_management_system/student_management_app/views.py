from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from django.contrib import messages
from student_management_app.EmailBackEnd import EmailBackEnd
from student_management_app import HodViews

# Create your views here.
def homePage(request):
    return render (request, 'home.html')

def loginPage(request):
    return render (request, 'login.html')

def registerPage(request):
    return render (request, 'register.html')

def registerUser(request):
    return HttpResponseRedirect('admin_home')


def logoutUser(request):
    logout(request, user)
