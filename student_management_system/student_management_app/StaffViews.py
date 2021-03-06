import json
from django.shortcuts import render, redirect
from django.contrib import messages
from student_management_app.models import CustomUser, Staffs, Subjects, SessionYear, Students, Attendance, AttendanceReport, LeaveReportStaff, FeedBackStaffs, StudentResult
from student_management_app.Forms import AddStaffForm, EditStaffForm, EditStudentResultForm, AddSubjectForm, EditSubjectForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.forms import model_to_dict
from django.views import View

def staffHome(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    students_count = Students.objects.filter().count()
    attendance_count = Attendance.objects.filter(subject_id__in=subjects).count()
    staff = Staffs.objects.get(admin=request.user.id)
    leave_count = LeaveReportStaff.objects.filter(staff_id=staff.id, leave_status=1).count()
    subjects_count = subjects.count()

    #Fetch Attendance Data by Subject
    subject_list = []
    attendance_list = []
    for subject in subjects:
        attendance_count1 = Attendance.objects.filter(subject_id=subject.id).count()
        subject_list.append(subject.subject_name)
        attendance_list.append(attendance_count1)
    
    students_attendance = Students.objects.all()
    student_list = []
    student_list_attendance_present = []
    student_list_attendance_absent = []
    for students in students_attendance:
        attendance_present_count = AttendanceReport.objects.filter(status=1, student_id=students.id).count()
        attendance_absent_count = AttendanceReport.objects.filter(status=0, student_id=students.id).count()
        student_list.append(students.admin.username)
        student_list_attendance_present.append(attendance_present_count)
        student_list_attendance_absent.append(attendance_absent_count)

    context = {
        'students_count':students_count,
        'attendance_count':attendance_count,
        'leave_count':leave_count,
        'subjects_count':subjects_count,
        'subject_list':subject_list,
        'attendance_list':attendance_list,
        'student_list':student_list,
        'present_list':student_list_attendance_present,
        'absent_list':student_list_attendance_absent
    }
    return render(request, 'staff_templates/home_content.html', context)

def editStaffProfile(request):
    user = CustomUser.objects.get(id=request.user.id)
    staff = Staffs.objects.get(admin=user)
    return render(request, 'staff_templates/edit-staff-profile-template.html', {'user':user, 'staff':staff})

def editStaffProfileSave(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        password = request.POST['password']
        try: 
            custommuser = CustomUser.objects.get(id=request.user.id)
            custommuser.first_name = first_name
            custommuser.last_name = last_name
            if password != None and password != "":
                custommuser.set_password = password
            custommuser.save()
            staff = Staffs.objects.get(admin=custommuser)
            staff.address = address
            staff.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('edit-staff-profile')
        except:
            messages.error(request, 'Failed to edit profile')
            return redirect('edit-staff-profile')

    else:
        return HttpResponse('Method not allowed')

def addStaff(request):
    form = AddStaffForm()
    return render(request, 'staff_templates/add-staff-template.html', {'form':form})

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
                
                messages.success(request, '{} Created Successfully'.format(username))
                return redirect('add-staff')
            except:
                messages.error(request, 'Failed to Create new Staff')
                return redirect('add-staff')
        else:
            form = AddStaffForm(request.POST)
            return render(request, 'staff_templates/add_staff_template.html', {'form':form})    
    else:
        return render(request, 'staff_templates/add_staff_template.html')

def manageStaff(request):
    staffs = Staffs.objects.all()
    return render(request, 'staff_templates/manage-staff-template.html', {'staffs':staffs})

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
    form.fields['address'].initial = staff.address
    form.fields['state'].initial = staff.state
    form.fields['nationality'].initial = staff.nationality
    
    return render(request, 'staff_templates/edit-staff-template.html', {'staff':staff, 'id':staff_id, 'form':form})

def editStaffSave(request):
    if request.method == 'POST':
        staff_id = request.session.get('staff_id')
        if staff_id == None:
            messages.info(request, 'Invalid Staff ID')
            return redirect('manage-student')
        form = EditStaffForm(request.POST)
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
                staff_model.address = address
                staff_model.state = state
                staff_model.nationality = nationality
                staff_model.save()
                del request.session['staff_id']
                messages.success(request, '{} Updated Successfully'.format(username))
                return redirect('manage-staff')
            except:
                messages.error(request, 'Failed to Edit {}'.format(username))
                return redirect('manage-staff')
        else:
            form = EditStaffForm(request.POST)
            messages.info('Failed to Edit Staff')
            return redirect('manage-staff')
    else:
        return render(request, 'staff_templates/edit_staff_template.html')

def addSubject(request):
    form = AddSubjectForm()
    return render(request, 'staff_templates/add-subject-template.html', {'form':form})    

def addSubjectSave(request):
    if request.method == 'POST':
        form = AddSubjectForm(request.POST)
        if form.is_valid():
            subject_name = form.cleaned_data['subject_name']
            subject_status = form.cleaned_data['subject_status']
            classs = form.cleaned_data['classs']
            staff_id = form.cleaned_data['staff_id']
            try:
                staffidd = CustomUser.objects.get(id=staff_id)
                new_subject = Subjects(subject_name=subject_name,subject_status=subject_status,classs=classs,staff_id=staffidd)

                new_subject.save()
                messages.success(request, '{} added successfully'.format(subject_name))
                return redirect('/add-subject')
            except:
                messages.error(request, 'Failed to add new subject')
                return redirect('/add-subject')
        else:
            form = AddSubjectForm(request.POST)
            return render(request, 'staff_templates/add-subject-template.html', {'form':form})    
    else:
        return HttpResponse('Method not allowed')

def manageSubject(request):
    subjects = Subjects.objects.all()
    return render(request, 'staff_templates/manage-subject-template.html', {'subjects':subjects})

def editSubject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    form = EditSubjectForm()
    form.fields['subject_name'].initial = subject.subject_name
    form.fields['subject_status'].initial = subject.subject_status
    form.fields['classs'].initial = subject.classs
    form.fields['staff_id'].initial = subject.staff_id
    return render(request, 'staff_templates/edit-subject-template.html', {'form':form, 'subject':subject})    

def editSubjectSave(request):
    if request.method == 'POST':
        form = EditSubjectForm(request.POST)
        if form.is_valid():
            subject_id = request.POST['subject_id']
            subject_name = form.cleaned_data['subject_name']
            subject_status = form.cleaned_data['subject_status']
            classs = form.cleaned_data['classs']
            staff_id = form.cleaned_data['staff_id']

            try:
                new_subject = Subjects.objects.get(id=subject_id)
                new_subject.subject_name = subject_name
                new_subject.subject_status = subject_status
                new_subject.classs = classs
                new_staff = CustomUser.objects.get(id=staff_id)
                new_subject.staff_id = new_staff
                new_staff.save()
                new_subject.save()


                messages.success(request, '{} Updated Successfully'.format(subject_name))
                return redirect('manage-subject')
            except:
                messages.error(request, 'Failed to Edit {}'.format(subject_name))
                return redirect('manage-subject')    
        else:
            form = EditSubjectForm(request.POST)
            return render(request, 'staff_templates/manage-subject-template.html', {'form':form})    
    else:
        return HttpResponse('Method not allowed')

def takeAttendance(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYear.objects.all()
    context = {
        'subjects':subjects,
        'session_years':session_years
        }
    return render(request, 'staff_templates/take-attendance-template.html', context)

@csrf_exempt
def get_students(request):
    subject_id = request.POST['subject']
    session_year = request.POST['session_year']

    subject = Subjects.objects.get(id=subject_id)
    session_model = SessionYear.objects.get(id=session_year)
    
    students = Students.objects.filter(session_year_id=session_model)

    list_data = []
    for student in students:
        data_small = {"id":student.admin.id,"name":student.admin.first_name+" "+student.admin.last_name}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_attendance_data(request):
    student_ids = request.POST['student_ids']
    subject_id = request.POST['subject_id']
    attendance_date = request.POST['attendance_date']
    session_year_id = request.POST['session_year_id']
    
    subject_model = Subjects.objects.get(id=subject_id)
    session_model = SessionYear.objects.get(id=session_year_id)
    json_student = json.loads(student_ids)
    #print(data[0]['id'])
    try: 
        attendance = Attendance(subject_id=subject_model, attendance_date=attendance_date, session_year_id=session_model)
        attendance.save()

        for stud in json_student:
            student = Students.objects.get(admin=stud['id'])
            attendance_report = AttendanceReport(student_id=student, attendance_id=attendance, status=stud['status'])
            attendance_report.save()
        return HttpResponse('Ok')
    except:
        return HttpResponse('Error Occured')

def update_attendance(request):
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_year_id = SessionYear.objects.all()
    context = {
        'subjects':subjects,
        'session_year_id':session_year_id
        }
    return render(request, 'staff_templates/update-attendance-template.html', context)

@csrf_exempt
def get_attendance_dates(request):
    subject = request.POST['subject']
    session_year_id = request.POST['session_year_id']
    subject_obj = Subjects.objects.get(id=subject)
    session_year_obj = SessionYear.objects.get(id=session_year_id)
    
    attendance = Attendance.objects.filter(subject_id=subject_obj,session_year_id=session_year_obj)
    attendance_obj = []

    for attendance_single in attendance:
        data = {"id":attendance_single.id, "attendance_date":str(attendance_single.attendance_date), "session_year_id":attendance_single.session_year_id.id}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj), safe=False)

@csrf_exempt
def get_student_attendance(request):
    attendance_date = request.POST['attendance_date']
    attendance = Attendance.objects.get(id=attendance_date)

    attendance_data = AttendanceReport.objects.filter(attendance_id=attendance)
    list_data = []
    for student in attendance_data:
        data_small = {"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_updated_attendance_data(request):
    student_ids = request.POST['student_ids']
    attendance_date = request.POST['attendance_date']
    attendance = Attendance.objects.get(id=attendance_date)
    
    json_student = json.loads(student_ids)
    
    try: 
        for stud in json_student:
            student = Students.objects.get(admin=stud['id'])
            attendance_report = AttendanceReport.objects.get(student_id=student, attendance_id=attendance)
            attendance_report.status = stud['status']
            attendance_report.save()
        return HttpResponse('Ok')
    except:
        return HttpResponse('Error Occured')

def applyLeave(request):
    staff_obj = Staffs.objects.get(admin=request.user.id)
    leave_data = LeaveReportStaff.objects.filter(staff_id=staff_obj)

    return render(request, 'staff_templates/apply-leave-template.html', {'leave_data':leave_data})

def applyLeaveSave(request):
    if request.method == 'POST':
        leave_date = request.POST['leave_date']
        leave_message = request.POST['leave_message']
        return_date = request.POST['return_date']

        staff_obj = Staffs.objects.get(admin=request.user.id)
        try: 
            leave_report = LeaveReportStaff(leave_date=leave_date, leave_message=leave_message, return_date=return_date, staff_id=staff_obj, leave_status=0)
            leave_report.save()
            messages.success(request, 'Application Submitted successfully')
            return redirect('staff-apply-leave')
        except:
            messages.error(request, 'Failed to apply for leave')
            return redirect('staff-apply-leave')

    else:
        return HttpResponse('Method not allowed')

def leaveFeedback(request):
    staff_obj = Staffs.objects.get(admin=request.user.id)
    feedback_data = FeedBackStaffs.objects.filter(staff_id=staff_obj)
    
    return render(request, 'staff_templates/leave-feedback-template.html', {'feedback_data':feedback_data}) 

def leaveFeedbackSave(request):
    if request.method == 'POST':
        
        feedback_message = request.POST['feedback_message']
        staff_obj = Staffs.objects.get(admin=request.user.id)

        try: 
            feedback_report = FeedBackStaffs(feedback=feedback_message, feedback_reply="", staff_id=staff_obj)
            feedback_report.save()
            messages.success(request, 'Feedback Submitted successfully')
            return redirect('staff-leave-feedback')
        except:
            messages.error(request, 'Failed to submit Feedback')
            return redirect('staff-leave-feedback')

    else:
        return HttpResponse('Method not allowed')

@csrf_exempt
def checkStaffEmailExist(request):
    email = request.POST['email']
    user_obj = CustomUser.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def checkStaffUsernameExist(request):
    username = request.POST['username']
    user_obj = CustomUser.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def staffFcmtokenSave(request):
    token = request.POST['token']
    try:
        staff = Staffs.objects.get(admin=request.user.id)
        staff.fcm_token = token
        staff.save()
        return HttpResponse('True')
    except:
        return HttpResponse('False')

def staffAddResult(request):                                           
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_years = SessionYear.objects.all()
    return render(request, 'staff_templates/add-result-template.html', {'subjects':subjects,'session_years':session_years})

def saveStudentResult(request):
    if request.method == 'POST':
        student_admin_id = request.POST['student_list']
        assignment_marks = request.POST['assignment_marks']
        exam_marks = request.POST['exam_marks']
        subject_id = request.POST['subject']
        
        student_obj = Students.objects.get(admin=student_admin_id)
        subject_obj = Subjects.objects.get(id=subject_id)
        try:
            check_exist = StudentResult.objects.filter(subject_id=subject_obj, student_id=student_obj,).exists()
            if check_exist:
                result = StudentResult.objects.get(student_id=student_obj, subject_id=subject_obj)
                result.subject_assignment_marks = subject_assignment_marks
                result.subject_exam_marks = subject_exam_marks
                result.save()
                messages.success(request, 'Successfully Updated Results')
                return redirect('staff-add-result')
            else:
                result = StudentResult(student_id=student_obj, subject_id=subject_obj, subject_exam_marks=exam_marks, subject_assignment_marks=assignment_marks)
                result.save()
                messages.success(request, 'Successfully Added Results')
                return redirect('staff-add-result')
        except:
            messages.error(request, 'Failed to Add Results')
            return redirect('staff-add-result')

    else:
        return HttpResponseRedirect('staff-add-result')

class editStudentResult(View):
    def get(self, request, *args, **kwargs):
        staff_id = request.user.id
        edit_result_form = EditStudentResultForm(staff_id=staff_id)
        return render(request, 'staff_templates/edit-result-template.html', {'form':edit_result_form})

    def post(self, request, *args, **kwargs):
        form = EditStudentResultForm(request.POST, staff_id=request.user.id)
        if form.is_valid():
            student_admin_id = form.cleaned_data['student_ids']
            assignment_marks = form.cleaned_data['assignment_marks']
            exam_marks = form.cleaned_data['exam_marks']
            subject_id = form.cleaned_data['subject_id']

            student_obj = Students.objects.get(admin=student_admin_id)
            subject_obj = Subjects.objects.get(id=subject_id)
            result = StudentResult.objects.get(student_id=student_obj, subject_id=subject_obj)
            result.subject_assignment_marks = assignment_marks
            result.subject_exam_marks = exam_marks
            result.save()
            messages.success(request, 'Successfully Updated Result')
            return redirect('edit-student-result')
        else:
            messages.error(request, 'Failed to Edit Result')
            form = EditStudentResultForm(request.POST, staff_id=request.user.id)
            return render(request, 'staff_templates/edit_result_template.html', {'form':form})

@csrf_exempt
def fetch_student_result(request):
    subject_id = request.POST['subject_id']
    student_id = request.POST['student_id']
    student_obj = Students.objects.get(admin=student_id)
    result =  StudentResult.objects.filter(student_id=student_obj.id, subject_id=subject_id).exists()
    if result:
        result = StudentResult.objects.get(student_id=student_obj.id, subject_id=subject_id)
        result_data = {"exam_marks":result.subject_exam_marks, "assignment_marks":result.subject_assignment_marks}
        return HttpResponse(json.dumps(result_data))
    else:
        return HttpResponse('False')
    