from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from student_management_app.models import Students
def studentHome(request):
    return render(request, 'student_templates/home_content.html')

def addStudent(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        #profile_picture = request.POST['profile_picture']
        address = request.POST['address']
        state = request.POST['state']
        nationality = request.POST['nationality']
        try:
            new_student = Students.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,date_of_birth=date_of_birth,email=email,phone_number=phone_number,gender=gender,address=address,state=state,nationality=nationality)
            new_student.save()
            messages.success(request, '{} added successfully'.format(first_name))
            return render(request, 'student_templates/add_student_template.html')   
        except:
            messages.error(request, 'Failed to add new student')
            return render(request, 'student_templates/add_student_template.html')    
    else:
        return render(request, 'student_templates/add_student_template.html')

def manageStudent(request):
    pass