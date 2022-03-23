from django.shortcuts import render, redirect
from accounts import urls
from django.http import HttpResponse
from student_management_app.models import SessionYear
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
    return render(request, 'hod_templates/add_session_template.html')

def addSessionSave(request):
    if request.method == 'POST':
        
        session_start_year = request.POST['session_start_year']
        session_end_year = request.POST['session_end_year']
        try:
            session = SessionYear(session_start_year=session_start_year,session_end_year=session_end_year)
            session.save()
            messages.success(request, 'Session Created Successfully')
            return redirect('admin-home')
        except:
            messages.error(request, 'Failed to add Session')
            return redirect('add-session')

    else:
        return HttpResponse('Method not allowed')

def editSession(request):
    form = EditSessionForm()
    return render(request, 'hod_templates/edit_session_template.html', {'form':form})

def editSessionSave(request):
    if request.method == 'POST':
        form = EditSessionForm(request.POST)
        if form.is_valid():
            term_start = form.cleaned_data['term_start']
            session_start = form.cleaned_data['session_start']
            term_end = form.cleaned_data['term_end']
            session_end = form.cleaned_data['session_end']

            try:
                new_session = Session.objects.create(session_start=session_start, session_end=session_end)
                new_session.save()
                return messages.success(request, 'Session edited successful')
                return redirect('admin-home')
            except:
                return messages.error(request, 'Failed to edit session')
                return redirect('edit-session')
        else:
            messages.error(request, 'Form is not valid')
            return redirect('edit-session')

    else:
        return HttpResponse('Method not allowed')

def studentFeedbackMessage(request):
    pass

def staffFeedbackMessage(request):
    pass