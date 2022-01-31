from django.shortcuts import render
from accounts import urls
def adminHome(request):

    return render(request, 'hod_templates/base.html')
def profile(request):

    return render(request, 'hod_templates/profile.html')
def contactUs(request):

    return render(request, 'hod_templates/contact-us.html')
def contacts(request):

    return render(request, 'hod_templates/contacts.html')