from django.shortcuts import render

def admin_home(request):

    return render(request, 'hod_templates/base.html')
def profile(request):

    return render(request, 'hod_templates/profile.html')
def contactUs(request):

    return render(request, 'hod_templates/contact-us.html')