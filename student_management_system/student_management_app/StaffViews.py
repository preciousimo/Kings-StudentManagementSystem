from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse

def staffHome(request):
    return render(request, 'staff_templates/home_content.html')

def addStaff(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        #profile_picture = request.POST['profile_picture']
        #curriculum_vitae = request.POST['curriculum_vitae']
        address = request.POST['address']
        state = request.POST['state']
        nationality = request.POST['nationality']
        return HttpResponse(first_name)
    else:
        return render(request, 'staff_templates/add_staff_template.html')
