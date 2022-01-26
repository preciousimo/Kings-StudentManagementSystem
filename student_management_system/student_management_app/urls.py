"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home)
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view())
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from student_management_app import views, HodViews, StudentViews, StaffViews


urlpatterns = [
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('register-user', views.registerUser),
    #path('login_user', views.loginUser),
    #path('get_user_details', views.getUserDetailserDetails),
    path('logout-user', views.logoutUser),
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
