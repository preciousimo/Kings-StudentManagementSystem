from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

def staffHome(request):
    return render(request, 'staff_templates/includes/home_content.html')

def addStaff(request):
    return render(request, 'staff_templates/add_staff_template.html')
