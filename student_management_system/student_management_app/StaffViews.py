from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

def staffHome(request):
    return render(request, 'staff_templates/home_content.html')

def addStaff(request):
    if request.method == 'POST':
        return HttpResponse('Posting in progress')
    else:
        return render(request, 'staff_templates/add_staff_template.html')
