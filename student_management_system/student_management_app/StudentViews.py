from django.shortcuts import render,redirect
from django.contrib import messages
from student_management_app.models import CustomUser, Students, SessionYear
from student_management_app.Forms import AddStudentForm, EditStudentForm
from django.http import HttpResponse, HttpResponseRedirect

def studentHome(request):
    return render(request, 'student_templates/home_content.html')

def addStudent(request):
    form = AddStudentForm()
    return render(request, 'student_templates/add_student_template.html', {'form':form})

def addStudentSave(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
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
            classs = form.cleaned_data['classs']
            session_year_id = form.cleaned_data['session_year_id']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            nationality = form.cleaned_data['nationality'] 
            try:
                new_student = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email, user_type=3)
        
                new_student.students.middle_name = middle_name
                new_student.students.date_of_birth = date_of_birth
                new_student.students.phone_number = phone_number
                new_student.students.gender = gender
                new_student.students.classs = classs
                session_year = SessionYear.objects.get(id=session_year_id)
                new_student.students.session_year_id = session_year
                new_student.students.address = address
                new_student.students.state = state
                new_student.students.nationality = nationality
                new_student.save()
                
                messages.success(request, '{} created successfully'.format(username))
                return redirect('add-student')
            except:
                messages.error(request, 'Failed to create new student')
                return redirect('add-student')
        else:
            form = AddStudentForm(request.POST)
            return render(request, 'student_templates/add_student_template.html', {'form':form})    
    else:
        return HttpResponse('Method not allowed')

def manageStudent(request):
    students = Students.objects.all()
    term = Term.objects.all()
    session = Session.objects.all()
    return render(request, 'student_templates/manage_student_template.html', {'students':students, 'term':term, 'session':session})

def editStudent(request, student_id):
    request.session['student_id'] = student_id
    student = Students.objects.get(admin=student_id)
    form = EditStudentForm()
    form.fields['first_name'].initial = student.admin.first_name
    form.fields['middle_name'].initial = student.middle_name
    form.fields['last_name'].initial = student.admin.last_name
    form.fields['username'].initial = student.admin.username
    form.fields['email'].initial = student.admin.email
    form.fields['date_of_birth'].initial = student.date_of_birth
    form.fields['gender'].initial = student.gender
    form.fields['phone_number'].initial = student.phone_number
    form.fields['address'].initial = student.address
    form.fields['state'].initial = student.state
    form.fields['classs'].initial = student.classs
    form.fields['nationality'].initial = student.nationality
    form.fields['term_start'].initial = student.term_start
    form.fields['session_start'].initial = student.session_start
    form.fields['term_end'].initial = student.term_end
    form.fields['session_end'].initial = student.session_end
    return render(request, 'student_templates/edit_student_template.html', {'student':student,'id':student_id,'form':form})

def editStudentSave(request):
    if request.method == 'POST':
        student_id = request.session.get('student_id')
        if student_id == None:
            return redirect('manage-student')
        form = EditStudentForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            date_of_birth = form.cleaned_data['date_of_birth']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            gender = form.cleaned_data['gender']
            address = form.cleaned_data['address']
            state = form.cleaned_data['state']
            nationality = form.cleaned_data['nationality']
            classs = form.cleaned_data['classs']
            term_start = form.cleaned_data['term_start']
            session_start = form.cleaned_data['session_start']
            term_end = form.cleaned_data['term_end']
            session_end = form.cleaned_data['session_end']
            try:
                user = CustomUser.objects.get(id=student_id)
                user.first_name = first_name
                user.last_name = last_name
                user.username = username
                user.email = email
                user.save()

                student_model = Students.objects.get(admin=student_id)
                student_model.middle_name = middle_name
                student_model.date_of_birth = date_of_birth
                student_model.phone_number = phone_number
                student_model.gender = gender
                student_model.address = address
                student_model.state = state
                student_model.nationality = nationality
                student_model.classs = classs
                student_model.term_start = term_start
                student_model.session_start = session_start
                student_model.term_end = term_end
                student_model.session_end = session_end
                student_model.save()
                del request.session['student_id']
                messages.success(request, '{} updated successfully'.format(username))
                return redirect('manage-student')
            except:
                messages.error(request, 'Failed to edit {}'.format(username))
                return redirect('manage-student')
        else:
            form = EditStudentForm(request.POST)
            return redirect('manage-student')
            messages.info('Failed to edit Student')
    else:
        return HttpResponse('Method not allowed')

def studentAttendance(request):
    return HttpResponse('Student Attendance ..')