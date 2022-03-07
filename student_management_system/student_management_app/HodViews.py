from django.shortcuts import render
from accounts import urls
from student_management_app.Forms import AddSessionForm
def adminHome(request):
    return render(request, 'hod_templates/home_content.html')

def profile(request):

    return render(request, 'hod_templates/profile.html')
def contactUs(request):

    return render(request, 'hod_templates/contact-us.html')
def contacts(request):

    return render(request, 'hod_templates/contacts.html')
def addSession(request):
    form = AddSessionForm()
    return render(request, 'hod_templates/add_session_template.html', {'form':form})
def manageSession(request):

    return render(request, 'hod_templates/manage_session_template.html')