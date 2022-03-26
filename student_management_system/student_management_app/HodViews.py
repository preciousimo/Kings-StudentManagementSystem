import json
from django.shortcuts import render, redirect
from accounts import urls
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from student_management_app.models import SessionYear, FeedBackStudents, FeedBackStaffs, LeaveReportStudent, LeaveReportStaff, Attendance, Subjects
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

def adminHome(request):
    return render(request, 'hod_templates/home_content.html')

def profile(request):
    return render(request, 'hod_templates/profile.html')

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
    subjects = Subjects.objects.filter(staff_id=request.user.id)
    session_year_id = SessionYear.objects.all()
    context = {
        'subjects':subjects,
        'session_year_id':session_year_id
        }
    return render(request, 'hod_templates/admin_view_attendance_template.html', context)


@csrf_exempt
def getAttendanceDates(request):
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

