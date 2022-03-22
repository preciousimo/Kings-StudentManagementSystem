from django.urls import path, include
from student_management_app import views, HodViews, StudentViews, StaffViews


urlpatterns = [
    
    #HOD/Admin Views
    path('admin-home', HodViews.adminHome, name="admin-home"),
    path('profile', HodViews.profile, name="profile"),
    path('contact-us', HodViews.contactUs, name="contact-us"),
    path('contacts', HodViews.contacts, name="contacts"),
    path('add-session', HodViews.addSession, name="add-session"),
    path('add-session-save', HodViews.addSessionSave, name="add-session-save"),
    path('edit-session', HodViews.editSession, name="edit-session"),
    path('edit-session-save', HodViews.editSessionSave, name="edit-session-save"),
    #Student Views
    path('student-home', StudentViews.studentHome, name="student-home"),
    path('add-student/', StudentViews.addStudent, name="add-student"),
    path('add-student-save/', StudentViews.addStudentSave, name="add-student-save"),
    path('manage-student/', StudentViews.manageStudent, name="manage-student"),
    path('edit-student/<str:student_id>', StudentViews.editStudent, name="edit-student"),
    path('edit-student-save/', StudentViews.editStudentSave, name="edit-student-save"),
    path('student-attendance/', StudentViews.studentAttendance, name="student-attendance"),
    path('student-view-attendance/', StudentViews.studentViewAttendance, name="student-view-attendance"),
    #Staff Views
    path('staff-home/', StaffViews.staffHome, name="staff-home"),
    path('add-staff/', StaffViews.addStaff, name="add-staff"),
    path('add-staff-save/', StaffViews.addStaffSave, name="add-staff-save"),
    path('manage-staff/', StaffViews.manageStaff, name="manage-staff"),
    path('add-subject/', StaffViews.addSubject, name="add-subject"),
    path('add-subject-save/', StaffViews.addSubjectSave, name="add-subject-save"),
    path('manage-subject/', StaffViews.manageSubject, name="manage-subject"),
    path('edit-staff/<str:staff_id>', StaffViews.editStaff, name="edit-staff"),
    path('edit-staff-save/', StaffViews.editStaffSave, name="edit-staff-save"),
    path('take-attendance/', StaffViews.takeAttendance, name="take-attendance"),
    path('get_students', StaffViews.get_students, name="get_students"),
    path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_student_attendance', StaffViews.get_student_attendance, name="get_student_attendance"),
    path('update_attendance', StaffViews.update_attendance, name="update_attendance"),
    path('save_updated_attendance_data', StaffViews.save_updated_attendance_data, name="save_updated_attendance_data"),
    path('apply-leave', StaffViews.applyLeave, name="apply-leave"),
    path('apply-leave-save', StaffViews.applyLeaveSave, name="apply-leave-save"),
    path('leave-feedback', StaffViews.leaveFeedback, name="leave-feedback"),
    path('leave-feedback-save', StaffViews.leaveFeedbackSave, name="leave-feedback-save"),
    
    
]
