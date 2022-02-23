from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from student_management_app.models import CustomUser, Staffs
from django.core.files.storage import FileSystemStorage
from student_management_app.Forms import AddStaffForm
def staffHome(request):
    return render(request, 'staff_templates/home_content.html')

def addStaff(request):
    form = AddStaffForm()
    return render(request, 'staff_templates/add_staff_template.html', {'form':form})

def addStaffSave(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        address = request.POST['address']
        state = request.POST['state']
        nationality = request.POST['nationality']
        profile_picture = request.FILES['profile_picture']
        fs = FileSystemStorage()
        filename = fs.save(profile_picture.name,profile_picture)
        profile_picture_url = fs.url(filename)

        try:
            new_staff = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email, user_type=2)
            new_staff.staffs.middle_name = middle_name
            new_staff.staffs.date_of_birth = date_of_birth
            new_staff.staffs.phone_number = phone_number
            new_staff.staffs.gender = gender
            new_staff.staffs.profile_picture = profile_picture_url
            new_staff.staffs.address = address
            new_staff.staffs.state = state
            new_staff.staffs.nationality = nationality
            new_staff.save()
            messages.success(request, '{} created successfully'.format(username))
            return redirect('/add-staff')   
        except:
            messages.error(request, 'Failed to add new staff')
            return redirect('/add-staff')   
    else:
        return render(request, 'staff_templates/add_staff_template.html')

def manageStaff(request):
    staffs = Staffs.objects.all()
    return render(request, 'staff_templates/manage_staff_template.html', {'staffs':staffs})

def editStaff(request, staff_id):
    staff = Staffs.objects.get(admin=staff_id)
    return render(request, 'staff_templates/edit_staff_template.html', {'staff':staff, 'id':staff_id})

def editStaffSave(request):
    if request.method == 'POST':
        staff_id = request.POST['staff_id']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        if request.FILES['profile_picture']:
            profile_picture = request.FILES.get('profile_picture',False)
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name,profile_picture)
            profile_picture_url = fs.url(filename)
        profile_picture = request.POST['profile_picture']
        if request.FILES.get('curicculum_vitae', False):
            curicculum_vitae = request.FILES['curicculum_vitae']
            fs = FileSystemStorage()
            filename = fs.save(curicculum_vitae.name,curicculum_vitae)
            curicculum_vitae_url = fs.url(filename)
        curicculum_vitae = request.POST['curicculum_vitae']
        address = request.POST['address']
        state = request.POST['state']
        nationality = request.POST['nationality']
        try:
            user = CustomUser.objects.get(id=staff_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username

            user.email = email
            user.save()

            staff_model = Staffs.objects.get(admin=staff_id)
            staff_model.middle_name = middle_name
            staff_model.date_of_birth = date_of_birth
            staff_model.phone_number = phone_number
            staff_model.gender = gender
            if profile_picture_url != None:
                staff_model.profile_picture = profile_picture_url
            staff_model.curicculum_vitae = curicculum_vitae_url
            staff_model.address = address
            staff_model.state = state
            staff_model.nationality = nationality
            staff_model.save()

            messages.success(request, '{} updated successfully'.format(username))
            return HttpResponseRedirect('/manage-staff')
        except:
            messages.error(request, 'Failed to edit {}'.format(username))
            return HttpResponseRedirect('/manage-staff')
    else:
        return render(request, 'staff_templates/edit_staff_template.html')

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
        return HttpResponse('Method not allowed')
        #return render(request, 'staff_templates/add_subject_template.html')    

def manageSubject(request):
    subjects = Subjects.objects.all()
    return render(request, 'staff_templates/manage_subject_template.html', {'subjects':subjects})