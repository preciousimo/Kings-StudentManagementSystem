from django.shortcuts import render
def staff_home(request):

    return render(request, 'staff_templates/base.html')

def add_staff(request):

    return render(request, 'staff_templates/add_staff_template.html')