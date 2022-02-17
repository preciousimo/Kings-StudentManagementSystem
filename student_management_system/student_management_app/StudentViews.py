from django.shortcuts import render,redirect
from django.contrib import messages
from student_management_app.models import CustomUser, Students
from django.http import HttpResponse, HttpResponseRedirect

def studentHome(request):
    return render(request, 'student_templates/home_content.html')

def addStudent(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        #profile_picture = request.POST['profile_picture']
        address = request.POST['address']
        state = request.POST['state']
        nationality = request.POST['nationality']
        term_start = request.POST['term_start']
        term_end = request.POST['term_end']
        session_start = request.POST['session_start']
        session_end = request.POST['session_end']
        try:
            new_student = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password, user_type=3)
            new_student.students.middle_name = middle_name
            new_student.students.date_of_birth = date_of_birth
            new_student.students.phone_number = phone_number
            new_student.students.gender = gender
            new_student.students.address = address
            new_student.students.state = state
            new_student.students.nationality = nationality
            new_student.students.term_start = term_start
            new_student.students.term_end = term_end
            new_student.students.session_start = session_start
            new_student.students.session_end = session_end
            new_student.save()
            messages.success(request, '{} added successfully'.format(username))
            return render(request, 'student_templates/add_student_template.html')   
        except:
            messages.error(request, 'Failed to add new student')
            return render(request, 'student_templates/add_student_template.html')
    else:
        return render(request, 'student_templates/add_student_template.html')    
    
def manageStudent(request):
    students = Students.objects.all()
    return render(request, 'student_templates/manage_student_template.html', {'students':students})

def editStudent(request, student_id):
    student = Students.objects.get(admin=student_id)
    return render(request, 'student_templates/edit_student_template.html', {'student':student})

def editStudentSave(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        date_of_birth = request.POST['date_of_birth']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gender = request.POST['gender']
        #profile_picture = request.POST['profile_picture']
        #curriculum_vitae = request.POST['curriculum_vitae']
        address = request.POST['address']
        state = request.POST['state']
        nationality = request.POST['nationality']
        term_start = request.POST['term_start']
        session_start = request.POST['session_start']
        term_end = request.POST['term_end']
        session_end = request.POST['session_end']
        try:
            user = CustomUser.objects.get(id=student_id)
            user.first_name = first_name
            user.last_name = last_name
            user.username = username
            user.email = email
            user.save()

            student_model = Students.objects.get(admin=student_id)
            student_model.middle_name = middle_name
            student_model.date_of_birth = date_of_birth
            student_model.phone_number = phone_number
            student_model.gender = gender
            student_model.address = address
            student_model.state = state
            student_model.nationality = nationality
            student_model.term_start = term_start
            student_model.session_start = session_start
            student_model.term_end = term_end
            student_model.session_end = session_end
            student_model.save()

            messages.success(request, '{} updated successfully'.format(username))
            return HttpResponseRedirect('/manage-student')
        except:
            messages.error(request, 'Failed to edit {}'.format(username))
            return HttpResponseRedirect('/manage-student')
    else:
        return render(request, 'student_templates/edit_student_template.html')



def studentAttendance(request):
    return HttpResponse('Student Attendance ..')