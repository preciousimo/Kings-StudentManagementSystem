from django.shortcuts import render, redirect
from accounts import urls
from student_management_app.Forms import AddTermForm, EditTermForm, AddSessionForm, EditSessionForm
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

def addTerm(request):
    form = AddTermForm()
    return render(request, 'hod_templates/add_term_template.html', {'form':form})

def addTermSave(request):
    if request.method == 'POST':
        form = AddTermForm(request.POST)
        if form.is_valid():
            term_start = form.cleaned_data['term_start']
            term_end = form.cleaned_data['term_end']
            try:
                term = Term.objects.create(term_start=term_start,term_end=term_end)
                term.save()
                messages.success(request, 'Term Created Successfully')
                return redirect('add-term')
            except:
                messages.error(request, 'Failed to add Term')
                return redirect('add-term')
        else:
            messages.error(request, 'Form is not valid')
            return redirect('/add-term')

    else:
        return HttpResponse('Method not allowed')

def addSession(request):
    form = AddSessionForm()
    return render(request, 'hod_templates/add_session_template.html', {'form':form})

def addSessionSave(request):
    if request.method == 'POST':
        form = AddSessionForm(request.POST)
        if form.is_valid():
            session_start = form.cleaned_data['session_start']
            session_end = form.cleaned_data['session_end']
            try:
                session = Session.objects.create(session_start=session_start,session_end=session_end)
                session.save()
                messages.success(request, 'Session Created Successfully')
                return redirect('add-session')
            except:
                messages.error(request, 'Failed to add Session')
                return redirect('add-session')
        else:
            messages.error(request, 'Form is not valid')
            return redirect('add-session')

    else:
        return HttpResponse('Method not allowed')

def editTerm(request):
    form = EditSessionForm()
    return render(request, 'hod_templates/edit_session_template.html', {'form':form})

def editTermSave(request):
    if request.method == 'POST':
        form = EditTermForm(request.POST)
        if form.is_valid():
            term_start = form.cleaned_data['term_start']
            term_end = form.cleaned_data['term_end']

            try:
                new_term = Term.objects.create(term_start=term_start, term_end=term_end)
                new_term.save()
                return messages.success(request, 'term edited successful')
                return redirect('admin-home')
            except:
                return messages.error(request, 'Failed to edit term')
                return redirect('edit-term')

        else:
            messages.error(request, 'Form is not valid')
            return redirect('edit-term')

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