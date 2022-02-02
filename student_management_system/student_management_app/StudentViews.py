from django.shortcuts import render
def studentHome(request):
    return render(request, 'student_templates/base.html')
def addStudent(request):
    return render(request, 'student_templates/add_staff_template.html')