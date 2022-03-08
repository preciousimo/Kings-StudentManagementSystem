from django.shortcuts import render
from accounts import urls
from student_management_app.Forms import AddSessionForm
from django.http import HttpResponse
from student_management_app.models import Session
from django.contrib import messages

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

def addSessionSave(request):
    if request.method == 'POST':
        form = AddSessionForm(request.POST)
        if form.is_valid():
            term_start = form.cleaned_data['term_start']
            session_start = form.cleaned_data['session_start']
            term_end = form.cleaned_data['term_end']
            session_end = form.cleaned_data['session_end']
            try:
                session = Session.objects.create_user(term_start=term_start,session_start=session_start,term_end=term_end,session_end=session_end)
                session.save()
                messages.success(request, 'Session Created Successfully')
                return redirect('add-session')
            except:
                messages.error(request, 'Failed to add Session')
                return redirect('add-session')

    else:
        return HttpResponse('Method not allowed')

def manageSession(request):

    return render(request, 'hod_templates/manage_session_template.html')