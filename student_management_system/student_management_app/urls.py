"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from student_management_app import views, HodViews, StudentViews, StaffViews


urlpatterns = [
    path('', views.homePage, name='home'),
    path('login/', views.loginPage, name='login'),
    path('login_user', views.loginUser, name='login'),
    path('get_user_details', views.getUserDetails, name='getUserDetails'),
    path('logout_user', views.logoutUser, name='logout'),
    #HOD/Admin Views
    path('admin_home', HodViews.admin_home, name='admin_home'),
    #Student Views
    path('student_home', StudentViews.student_home, name='student_home'),
    #Staff Views
    path('staff_home/', StaffViews.staff_home),
    path('add_staff/', StaffViews.add_staff),
    path('add_staff_save', StaffViews.add_staff_save)
]
