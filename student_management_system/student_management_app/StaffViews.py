from django.shortcuts import render, redirect
from django.contrib import messages
from student_management_app.models import CustomUser, Staffs, Subjects
from student_management_app.Forms import AddStaffForm, EditStaffForm
from django.http import HttpResponse

def staffHome(request):
    return render(request, 'staff_templates/home_content.html')

def addStaff(request):
    form = AddStaffForm()
    return render(request, 'staff_templates/add_staff_template.html', {'form':form})

def addStaffSave(request):
    if request.method == 'POST':
        form = AddStaffForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            nationality = form.cleaned_data['nationality']             
            try:
                new_staff = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email, user_type=2)

                new_staff.staffs.middle_name = middle_name
                new_staff.staffs.date_of_birth = date_of_birth
                new_staff.staffs.phone_number = phone_number
                new_staff.staffs.gender = gender
                new_staff.staffs.address = address
                new_staff.staffs.state = state
                new_staff.staffs.nationality = nationality
                new_staff.save()
                
                messages.success(request, '{} created successfully'.format(username))
                return redirect('add-staff')
            except:
                messages.error(request, 'Failed to create new staff')
                return redirect('add-staff')
        else:
            form = AddStaffForm(request.POST)
            return render(request, 'staff_templates/add_staff_template.html', {'form':form})    
    else:
        return render(request, 'staff_templates/add_staff_template.html')

def manageStaff(request):
    staffs = Staffs.objects.all()
    return render(request, 'staff_templates/manage_staff_template.html', {'staffs':staffs})

def editStaff(request, staff_id):
    request.session['staff_id'] = staff_id
    staff = Staffs.objects.get(admin=staff_id)
    form = EditStaffForm()
    form.fields['first_name'].initial = staff.admin.first_name
    form.fields['middle_name'].initial = staff.middle_name
    form.fields['last_name'].initial = staff.admin.last_name
    form.fields['username'].initial = staff.admin.username
    form.fields['email'].initial = staff.admin.email
    form.fields['date_of_birth'].initial = staff.date_of_birth
    form.fields['gender'].initial = staff.gender
    form.fields['phone_number'].initial = staff.phone_number
    form.fields['profile_picture'].initial = staff.profile_picture
    form.fields['curriculum_vitae'].initial = staff.curriculum_vitae
    form.fields['address'].initial = staff.address
    form.fields['state'].initial = staff.state
    form.fields['nationality'].initial = staff.nationality
    
    return render(request, 'staff_templates/edit_staff_template.html', {'staff':staff, 'id':staff_id, 'form':form})

def editStaffSave(request):
    if request.method == 'POST':
        staff_id = request.session.get('staff_id')
        if staff_id == None:
            return redirect('manage-student')
        form = EditStaffForm(request.POST, request.FILES)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            if request.FILES['profile_picture']:
                profile_picture = request.FILES.get('profile_picture',False)
                fs = FileSystemStorage()
                filename = fs.save(profile_picture.name,profile_picture)
                profile_picture_url = fs.url(filename)
            profile_picture = form.cleaned_data['profile_picture']
            if request.FILES.get('curriculum_vitae', False):
                curriculum_vitae = request.FILES['curriculum_vitae']
                fs = FileSystemStorage()
                filename = fs.save(curriculum_vitae.name,curriculum_vitae)
                curriculum_vitae_url = fs.url(filename)
            curriculum_vitae = form.cleaned_data['curriculum_vitae']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            nationality = form.cleaned_data['nationality']
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
                staff_model.curriculum_vitae = curriculum_vitae_url
                staff_model.address = address
                staff_model.state = state
                staff_model.nationality = nationality
                staff_model.save()
                del request.session['student_id']
                messages.success(request, '{} updated successfully'.format(username))
                return redirect('manage-staff')
            except:
                messages.error(request, 'Failed to edit {}'.format(username))
                return redirect('manage-staff')
        else:
            form = EditStaffForm(request.POST)
            return redirect('manage-staff')
            messages.info('Failed to edit Staff')
    else:
        return render(request, 'staff_templates/edit_staff_template.html')

def addSubject(request):
    staffs = CustomUser.objects.filter(user_type=2)
    return render(request, 'staff_templates/add_subject_template.html', {'staffs':staffs})    

def addSubjectSave(request):
    if request.method == 'POST':
        subject_name = request.POST['subject_name']
        subject_status = request.POST['subject_status']
        classs = request.POST['classs']
        staff_id = request.POST['staff']
        staff = CustomUser.objects.get(id=staff_id)
        try:
            new_subject = Subjects(subject_name=subject_name,subject_status=subject_status,classs=classs,staff_id=staff)
            new_subject.save()
            messages.success(request, '{} added successfully'.format(subject_name))
            return redirect('/add-subject')
        except:
            messages.error(request, 'Failed to add new subject')
            return redirect('/add-subject')
    else:
        return HttpResponse('Method not allowed')

def manageSubject(request):
    subjects = Subjects.objects.all()
    return render(request, 'staff_templates/manage_subject_template.html', {'subjects':subjects})

def takeAttendance(request):
    pass