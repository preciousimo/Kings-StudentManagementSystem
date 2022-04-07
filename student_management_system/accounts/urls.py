from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('check-admin-email-exist', views.checkAdminEmailExist, name="check-admin-email-exist"),
    path('check-admin-username-exist', views.checkAdminUsernameExist, name="check-admin-username-exist"),
    path('logout/', views.logoutPage, name="logout"),
]
