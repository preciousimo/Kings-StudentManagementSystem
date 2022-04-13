import json
from django.shortcuts import render, redirect
from accounts import urls
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from student_management_app.models import SessionYear, FeedBackStudents, FeedBackStaffs, LeaveReportStudent, LeaveReportStaff, Attendance, Subjects, AttendanceReport, CustomUser, Students, Staffs
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def adminHome(request):
    students_count = Students.objects.all().count()
    staffs_count = Students.objects.all().count()
    subjects_count = Subjects.objects.all().count()

    subjects_all = Subjects.objects.all()
    subject_list = []
    student_count_list_in_subject = []
    for subject in subjects_all:
        student_count = Students.objects.filter(id=subject.id).count()
        subject_list.append(subject.subject_name)
        student_count_list_in_subject.append(student_count)

    staffs = Staffs.objects.all()
    attendance_present_list_staff = []
    attendance_absent_list_staff = []
    staff_name_list = []
    for staff in staffs:
        subject_ids = Subjects.objects.filter(staff_id=staff.admin.id)
        attendance = Attendance.objects.filter(subject_id__in=subject_ids).count()
        leaves = LeaveReportStaff.objects.filter(staff_id=staff.id, leave_status=1).count()
        attendance_present_list_staff.append(attendance)
        attendance_absent_list_staff.append(leaves)
        staff_name_list.append(staff.admin.username)
    
    students = Students.objects.all()
    attendance_present_list_student = []
    attendance_absent_list_student = []
    student_name_list = []
    for student in students:
        attendance = AttendanceReport.objects.filter(student_id=student.id, status=True).count()
        absent = AttendanceReport.objects.filter(student_id=student.id, status=False).count()
        leaves = LeaveReportStudent.objects.filter(student_id=student.id, leave_status=1).count()
        attendance_present_list_student.append(attendance)
        attendance_absent_list_student.append(leaves+absent)
        student_name_list.append(student.admin.username)

    
    context = {
        'students_count':students_count,
        'staffs_count':staffs_count,
        'subjects_count':subjects_count,
        'subject_list':subject_list,
        'student_count_list_in_subject':student_count_list_in_subject,
        'attendance_present_list_staff':attendance_present_list_staff,
        'attendance_absent_list_staff':attendance_absent_list_staff,
        'staff_name_list':staff_name_list,
        'attendance_present_list_student':attendance_present_list_student,
        'attendance_absent_list_student':attendance_absent_list_student,
        'student_name_list':student_name_list
    }
    return render(request, 'hod_templates/home_content.html', context)

def adminStudentHome(request):
    student_obj = CustomUser.objects.get(user_type=3)
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



def adminProfile(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'hod_templates/admin_profile_template.html', {'user':user})

def editAdminProfile(request):
    user = CustomUser.objects.get(id=request.user.id)
    return render(request, 'hod_templates/edit_admin_profile_template.html', {'user':user})

def editAdminProfileSave(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        try: 
            custommuser = CustomUser.objects.get(id=request.user.id)
            custommuser.first_name = first_name
            custommuser.last_name = last_name
            if password != None and password != "":
                custommuser.set_password = password
            custommuser.save()

            messages.success(request, 'Profile Updated Successfully')
            return redirect('edit-admin-profile')
        except:
            messages.error(request, 'Failed to edit profile')
            return redirect('edit-admin-profile')

    else:
        return HttpResponse('Method not allowed')

def contactUs(request):
    return render(request, 'hod_templates/contact-us.html')

def contacts(request):
    return render(request, 'hod_templates/contacts.html')

def addSession(request):
    return render(request, 'hod_templates/add_session_template.html')

def addSessionSave(request):
    if request.method == 'POST':
        
        session_start_year = request.POST['session_start_year']
        session_end_year = request.POST['session_end_year']
        try:
            session = SessionYear(session_start_year=session_start_year,session_end_year=session_end_year)
            session.save()
            messages.success(request, 'Session Created Successfully')
            return redirect('admin-home')
        except:
            messages.error(request, 'Failed to add Session')
            return redirect('add-session')

    else:
        return HttpResponse('Method not allowed')

def editSession(request):
    form = EditSessionForm()
    return render(request, 'hod_templates/edit_session_template.html', {'form':form})

def editSessionSave(request):
    if request.method == 'POST':
        form = EditSessionForm(request.POST)
        if form.is_valid():
            term_start = form.cleaned_data['term_start']
            session_start = form.cleaned_data['session_start']
            term_end = form.cleaned_data['term_end']
            session_end = form.cleaned_data['session_end']

            try:
                new_session = Session.objects.create(session_start=session_start, session_end=session_end)
                new_session.save()
                return messages.success(request, 'Session edited successful')
                return redirect('admin-home')
            except:
                return messages.error(request, 'Failed to edit session')
                return redirect('edit-session')
        else:
            messages.error(request, 'Form is not valid')
            return redirect('edit-session')

    else:
        return HttpResponse('Method not allowed')

def studentFeedbackMessage(request):
    feedbacks = FeedBackStudents.objects.all()
    return render(request, 'hod_templates/student_feedback_message.html', {'feedbacks':feedbacks})

def staffFeedbackMessage(request):
    feedbacks = FeedBackStaffs.objects.all()
    return render(request, 'hod_templates/staff_feedback_message.html', {'feedbacks':feedbacks})
@csrf_exempt
def studentFeedbackReply(request):
    feedback_id = request.POST['id']
    feedback_message = request.POST['message']
    try:
        feedback = FeedBackStudents.objects.get(id = feedback_id)
        feedback.feedback_reply = feedback_message
        feedback.save()
        return HttpResponse('True')
    except:
        return HttpResponse('False')

def studentLeaveView(request):
    leaves = LeaveReportStudent.objects.all()
    return render(request, 'hod_templates/student_leave_view.html', {'leaves':leaves})

def staffLeaveView(request):
    leaves = LeaveReportStaff.objects.all()
    return render(request, 'hod_templates/staff_leave_view.html', {'leaves':leaves})

def studentApproveLeave(request, leave_id):
    leave = LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status = 1
    leave.save()
    return HttpResponseRedirect('/student-leave-view')

def studentDisapproveLeave(request, leave_id):
    leave = LeaveReportStudent.objects.get(id=leave_id)
    leave.leave_status = 2
    leave.save()
    return HttpResponseRedirect('/student-leave-view')

def staffApproveLeave(request, leave_id):
    leave = LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status = 1
    leave.save()
    return HttpResponseRedirect('/staff-leave-view')

def staffDisapproveLeave(request, leave_id):
    leave = LeaveReportStaff.objects.get(id=leave_id)
    leave.leave_status = 2
    leave.save()
    return HttpResponseRedirect('/staff-leave-view')

def adminViewAttendance(request):
    subjects = Subjects.objects.all()
    session_year_id = SessionYear.objects.all()
    context = {
        'subjects':subjects,
        'session_year_id':session_year_id
        }
    return render(request, 'hod_templates/admin_view_attendance_template.html', context)

@csrf_exempt
def adminGetAttendanceDates(request):
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
def adminGetStudentAttendance(request):
    attendance_date = request.POST['attendance_date']
    attendance = Attendance.objects.get(id=attendance_date)

    attendance_data = AttendanceReport.objects.filter(attendance_id=attendance)
    list_data = []
    for student in attendance_data:
        data_small = {"id":student.student_id.admin.id,"name":student.student_id.admin.first_name+" "+student.student_id.admin.last_name,"status":student.status}
        list_data.append(data_small)

    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)
