from django.shortcuts import render
def studentHome(request):
    return render(request, 'student_templates/base.html')