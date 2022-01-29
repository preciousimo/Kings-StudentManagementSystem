from django.urls import path
from student_management_app import views, HodViews, StudentViews, StaffViews


urlpatterns = [
    #HOD/Admin Views
    path('admin-home', HodViews.adminHome),
    path('profile', HodViews.profile),
    path('contact-us', HodViews.contactUs),
    #Student Views
    path('student-home', StudentViews.studentHome),
    #Staff Views
    path('staff-home/', StaffViews.staffHome),
    path('add-staff/', StaffViews.addStaff),
    #path('add_staff_save', StaffViews.add_staff_save)
]
