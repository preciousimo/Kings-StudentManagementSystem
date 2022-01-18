from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homePage(request):
    
    return render (request, 'home.html')

def loginPage(request):
    return render (request, 'login.html')

def login_user(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method not allowed</h2>")
    else:
        return HttpResponse("Email :"+request.POST.get('email')+ " Password:"+request.POST.get('password'))