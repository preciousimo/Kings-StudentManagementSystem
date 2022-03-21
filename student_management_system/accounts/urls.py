from django.urls import path, include
from accounts import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutPage, name="logout"),
    path('accounts/', include('django.contrib.auth.urls')),
]
