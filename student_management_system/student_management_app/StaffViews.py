from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from student_management_app.models import Staffs, Subjects, SchoolAdmin
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
        try:
            new_staff = Staffs.objects.create(first_name=first_name,middle_name=middle_name,last_name=last_name,date_of_birth=date_of_birth,email=email,phone_number=phone_number,gender=gender,address=address,state=state,nationality=nationality)
            new_staff.save()
            messages.success(request, '{} added successfully'.format(first_name))
            return render(request, 'staff_templates/add_staff_template.html')   
        except:
            messages.error(request, 'Failed to add new staff')
            return render(request, 'staff_templates/add_staff_template.html')    
    else:
        return render(request, 'staff_templates/add_staff_template.html')
   
def manageStaff(request):
    staffs = Staffs.objects.all()
    return render(request, 'staff_templates/manage_staff_template.html', {'staffs':staffs})

def addSubject(request):
    if request.method == 'POST':
        subject_name = request.POST['subject_name']
        subject_status = request.POST['subject_status']
        staff_id = request.POST.get('staff')
        staff = Staffs.objects.get(id)
        admin_id = request.POST['admin']
        admin = SchoolAdmin.objects.get(id=admin_id)
        
        try:
            new_subject = Subjects.objects.create(subject_name=subject_name,subject_status=subject_status,staff_id_id=staff_id,admin_id=admin_id)
            new_subject.save()
            messages.success(request, '{} added successfully'.format(subject_name))
            return render(request, 'staff_templates/add_subject_template.html')   
        except:
            messages.error(request, 'Failed to add new subject')
            return render(request, 'staff_templates/add_subject_template.html')    
    else:
        return render(request, 'staff_templates/add_subject_template.html')

def manageSubject(request):
    subjects = Subjects.objects.all()
    return render(request, 'staff_templates/manage_subject_template.html', {'subjects':subjects})
