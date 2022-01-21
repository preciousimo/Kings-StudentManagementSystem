from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from student_management_app.models import CustomUser


def staff_home(request):
    return render(request, 'staff_templates/includes/home_content.html')

def add_staff(request):
    return render(request, 'staff_templates/add_staff_template.html')

def add_staff_save(request):
    if request.method != 'POST':
        return HttpResponse('<h2>Method not allowed</h2>')
        return HttpResponseRedirect('staff_templates/add_staff_template.html')
    else:
        first_name = request.POST.get('first_name')
        second_name = request.POST.get('second_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        try:
            user = CustomUser.objects.create_user(first_name=first_name,second_name=second_name,username=username,email=email,password=password,user_type=2)
            user.staffs.address=address
            user.save()
            message.success(request, username+' added successfully')
            return HttpResponseRedirect('/add_staff')
        except:
            messages.error(request,'Failed to add staff')
            return HttpResponseRedirect('/add_staff')