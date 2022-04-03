from django.shortcuts import render,redirect
from django.contrib import messages
from student_management_app.models import CustomUser, Students, SessionYear, Subjects, Attendance, AttendanceReport, LeaveReportStudent, FeedBackStudents
from student_management_app.Forms import AddStudentForm, EditStudentForm
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.views.decorators.csrf import csrf_exempt

def studentHome(request):
    student_obj = Students.objects.get(admin=request.user.id)
    total_attendance = AttendanceReport.objects.filter(student_id=student_obj).count()
    present_attendance = AttendanceReport.objects.filter(student_id=student_obj,status=True).count()
    absent_attendance = AttendanceReport.objects.filter(student_id=student_obj,status=False).count()
    subjects = Subjects.objects.all().count()

    subject_name = []
    data_present = []
    data_absent = []
    subject_data = Subjects.objects.all()

    for subject in subject_data:
        attendance = Attendance.objects.filter(subject_id=subject.id)
        present_attendance_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=True, student_id=student_obj.id).count()
        absent_attendance_count = AttendanceReport.objects.filter(attendance_id__in=attendance, status=False, student_id=student_obj.id).count()
        subject_name.append(subject.subject_name)
        data_present.append(present_attendance_count)
        data_absent.append(absent_attendance_count)

    context = {
        'total_attendance':total_attendance,
        'present_attendance':present_attendance,
        'absent_attendance':absent_attendance,
        'subjects':subjects,
        'data_name':subject_name,
        'data1':data_present,
        'data2':data_absent,
    }
    return render(request, 'student_templates/home_content.html', context)

def editStudentProfile(request):
    user = CustomUser.objects.get(id=request.user.id)
    student = Students.objects.get(admin=user)
    return render(request, 'student_templates/edit_student_profile_template.html', {'user':user,'student':student})

def editStudentProfileSave(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        address = request.POST['address']
        try: 
            custommuser = CustomUser.objects.get(id=request.user.id)
            custommuser.first_name = first_name
            custommuser.last_name = last_name
            if password != None and password != "":
                custommuser.set_password = password
            custommuser.save()

            messages.success(request, 'Profile Updated Successfully')
            return redirect('edit-student-profile')
        except:
            messages.error(request, 'Failed to edit profile')
            return redirect('edit-student-profile')

    else:
        return HttpResponse('Method not allowed')

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
    return render(request, 'student_templates/manage_student_template.html', {'students':students})

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

def studentViewAttendance(request):
    student = Students.objects.filter(admin=request.user.id)
    subjects = Subjects.objects.all()

    context = {
        'subjects':subjects,
    }

    return render(request, 'student_templates/student_view_attendance.html', context)

def studentViewAttendanceSave(request):
    subject_id = request.POST['subject']
    start_date = request.POST['start_date']
    end_date = request.POST['end_date']

    start_data_parse = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
    end_data_parse = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
    subject_obj = Subjects.objects.get(id=subject_id)
    user_object = CustomUser.objects.get(id=request.user.id)
    student_obj = Students.objects.get(admin=user_object)

    attendance = Attendance.objects.filter(attendance_date__range=(start_data_parse,end_data_parse),subject_id=subject_obj)
    attendance_reports = AttendanceReport.objects.filter(attendance_id__in=attendance, student_id=student_obj)

    context = {
        'attendance':attendance,
        'attendance_reports':attendance_reports,
        'start_date':start_date,
        'end_date':end_date
    }

    return render(request, 'student_templates/student_attendance_data.html', context)

def applyLeave(request):
    student_obj = Students.objects.get(admin=request.user.id)
    leave_data = LeaveReportStudent.objects.filter(student_id=student_obj)

    return render(request, 'student_templates/apply_leave_template.html', {'leave_data':leave_data})

def applyLeaveSave(request):
    if request.method == 'POST':
        leave_date = request.POST['leave_date']
        leave_message = request.POST['leave_message']
        return_date = request.POST['return_date']

        student_obj = Students.objects.get(admin=request.user.id)
        try: 
            leave_report = LeaveReportStudent(leave_date=leave_date, leave_message=leave_message, return_date=return_date, student_id=student_obj, leave_status=0)
            leave_report.save()
            messages.success(request, 'Application Submitted successfully')
            return redirect('student-apply-leave')
        except:
            messages.error(request, 'Failed to apply for leave')
            return redirect('student-apply-leave')

    else:
        return HttpResponse('Method not allowed')

def leaveFeedback(request):
    student_obj = Students.objects.get(admin=request.user.id)
    feedback_data = FeedBackStudents.objects.filter(student_id=student_obj)
    
    return render(request, 'student_templates/leave_feedback_template.html', {'feedback_data':feedback_data}) 

def leaveFeedbackSave(request):
    if request.method == 'POST':
        
        feedback_message = request.POST['feedback_message']
        student_obj = Students.objects.get(admin=request.user.id)

        try: 
            feedback_report = FeedBackStudents(feedback=feedback_message, feedback_reply="", student_id=student_obj)
            feedback_report.save()
            messages.success(request, 'Feedback Submitted successfully')
            return redirect('student-leave-feedback')
        except:
            messages.error(request, 'Failed to submit Feedback')
            return redirect('student-leave-feedback')

    else:
        return HttpResponse('Method not allowed')

@csrf_exempt
def checkStudentEmailExist(request):
    email = request.POST['email']
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def checkStudentUsernameExist(request):
    username = request.POST['username']
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def studentFcmtokenSave(request):
    token = request.POST['token']
    try:
        student = Students.objects.get(admin=request.user.id)
        student.fcm_token = token
        student.save()
        return HttpResponse('True')
    except:
        return HttpResponse('False')
