from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.loginPage),
    path('register/', views.registerPage),
    path('logout/', views.logoutPage)
]
