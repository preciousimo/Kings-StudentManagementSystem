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
    #Staff Views
    path('staff-home/', StaffViews.staffHome),
    path('add-staff/', StaffViews.addStaff),
    
    
]
