from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages


def staff_home(request):
    return render(request, 'staff_templates/includes/home_content.html')

def add_staff(request):
    return render(request, 'staff_templates/add_staff_template.html')

def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method not allowed</h2>')
        return HttpResponseRedirect('staff_templates/add_staff_template.html')
    else:
        if request.POST.get == None:
            messages.error('Invalid Input')
        else:
            firstname = request.POST.get('firstname')
            secondname = request.POST.get('secondname')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            address = request.POST.get('address')
