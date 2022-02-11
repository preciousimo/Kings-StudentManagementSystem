from django.urls import path
from student_management_app import views, HodViews, StudentViews, StaffViews


urlpatterns = [
    #HOD/Admin Views
    path('admin-home', HodViews.adminHome),
    path('profile', HodViews.profile),
    path('contact-us', HodViews.contactUs),
    path('contacts', HodViews.contacts),
    #Student Views
    path('student-home', StudentViews.studentHome),
    path('add-student/', StudentViews.addStudent),
    path('manage-student/', StudentViews.manageStudent),
    path('student-attendance/', StudentViews.studentAttendance),
    #Staff Views
    path('staff-home/', StaffViews.staffHome),
    path('add-staff/', StaffViews.addStaff),
    path('manage-staff/', StaffViews.manageStaff),
    path('add-subject/', StaffViews.addSubject),
    path('manage-subject/', StaffViews.manageSubject),
    path('edit-staff/<str:staff_id>', StaffViews.editStaff)
    
]
