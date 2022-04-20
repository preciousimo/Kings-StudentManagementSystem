from django import forms
from django.forms import ChoiceField
from django.forms.widgets import TextInput, FileInput
from student_management_app.models import SessionYear, Subjects, CustomUser

class ChoiceNoValidation(ChoiceField):
    def validate(self, value):
        pass

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    middle_name = forms.CharField(label = "Middle Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    last_name = forms.CharField(label = "Last Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    username = forms.CharField(label = "Username",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    email = forms.EmailField(label = "Email",max_length=100, widget=forms.EmailInput(attrs={'class':'form-control','autocomplete':'off'}))
    password = forms.CharField(label = "Password",max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label = "Phone Number",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    gender_choice = (
        ('Others', 'Others'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(label = "Gender",choices=gender_choice, widget=forms.Select(attrs={'class':'form-control'}))
    classs_choice = (
        ('JSS1', 'JSS 1'),
        ('JSS2', 'JSS 2'),
        ('JSS3', 'JSS 3'),
        ('SSS1', 'SSS 1'),
        ('SSS2', 'SSS 2'),
        ('SSS3', 'SSS 3'),  
    )
    classs = forms.ChoiceField(label = "Class",choices=classs_choice, widget=forms.Select(attrs={'class':'form-control'}))
    session_list = []
    try:
        sessions = SessionYear.objects.all()
        for ses in sessions:
            small_ses = (ses.id, str(ses.session_start_year)+"  -  "+str(ses.session_end_year))
            session_list.append(small_ses)
    except:
        pass
    session_year_id = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={'class':'form-control'}))
    address = forms.CharField(label = "Address",max_length=500, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    state = forms.CharField(label = "State",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    nationality = forms.CharField(label = "Nationality", max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    
class EditStudentForm(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    middle_name = forms.CharField(label = "Middle Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label = "Username",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email",max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label = "Phone Number",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    gender_choice = (
        ('Others', 'Others'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(label = "Gender",choices=gender_choice, widget=forms.Select(attrs={'class':'form-control'}))
    address = forms.CharField(label = "Address",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label = "State",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    nationality = forms.CharField(label = "Nationality", max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    class_choice = (
        ('JSS1', 'JSS 1'),
        ('JSS2', 'JSS 2'),        
        ('JSS3', 'JSS 3'),
        ('SSS1', 'SSS 1'),
        ('SSS2', 'SSS 2'),
        ('SSS3', 'SSS 3'),
    )
    classs = forms.ChoiceField(label = "Class",choices=class_choice, widget=forms.Select(attrs={'class':'form-control'}))

class AddStaffForm(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    middle_name = forms.CharField(label = "Middle Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    last_name = forms.CharField(label = "Last Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    username = forms.CharField(label = "Username",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    email = forms.EmailField(label = "Email",max_length=50, widget=forms.EmailInput(attrs={'class':'form-control','autocomplete':'off'}))
    password = forms.CharField(label = "Password",max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label = "Phone Number",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    gender_choice = (
        ('Others', 'Others'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(label = "Gender",choices=gender_choice, widget=forms.Select(attrs={'class':'form-control'}))
    address = forms.CharField(label = "Address",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    state = forms.CharField(label = "State",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    nationality = forms.CharField(label = "Nationality", max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    
class EditStaffForm(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    middle_name = forms.CharField(label = "Middle Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label = "Username",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email",max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(widget=DateInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(label = "Phone Number",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    gender_choice = (
        ('Others', 'Others'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = forms.ChoiceField(label = "Gender",choices=gender_choice, widget=forms.Select(attrs={'class':'form-control'}))
    address = forms.CharField(label = "Address",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label = "State",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    nationality = forms.CharField(label = "Nationality", max_length=50, widget=TextInput(attrs={'class':'form-control'}))

class AddSubjectForm(forms.Form):
    subject_name = forms.CharField(label = "Subject Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    subject_status_choice = (
        ('General', 'General'),
        ('Elective', 'Elective'),
    )
    subject_status = forms.ChoiceField(label = "Subject Status",choices=subject_status_choice, widget=forms.Select(attrs={'class':'form-control'}))
    classs_choice = (
        ('JSS1', 'JSS 1'),
        ('JSS2', 'JSS 2'),
        ('JSS3', 'JSS 3'),
        ('SSS1', 'SSS 1'),
        ('SSS2', 'SSS 2'),
        ('SSS3', 'SSS 3'),  
    )
    staff_list = []
    staffs = CustomUser.objects.filter(user_type=2)
    try:
        for staff in staffs:
            staff_name = (staff.id, staff.username)
            staff_list.append(staff_name)    
    except:
        pass
    classs = forms.ChoiceField(label = "Class", choices=classs_choice, widget=forms.Select(attrs={'class':'form-control'}))  
    staff_id = forms.ChoiceField(label = "Staff", choices=staff_list, widget=forms.Select(attrs={'class':'form-control'}))  
    
class EditSubjectForm(forms.Form):
    subject_name = forms.CharField(label = "Subject Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    subject_status_choice = (
        ('General', 'General'),
        ('Elective', 'Elective'),
    )
    subject_status = forms.ChoiceField(label = "Subject Status",choices=subject_status_choice, widget=forms.Select(attrs={'class':'form-control'}))
    classs_choice = (
        ('JSS1', 'JSS 1'),
        ('JSS2', 'JSS 2'),
        ('JSS3', 'JSS 3'),
        ('SSS1', 'SSS 1'),
        ('SSS2', 'SSS 2'),
        ('SSS3', 'SSS 3'),  
    )
    classs = forms.ChoiceField(label = "Class", choices=classs_choice, widget=forms.Select(attrs={'class':'form-control'}))  
    staff_list = []
    staffs = CustomUser.objects.filter(user_type=2)
    try:
        for staff in staffs:
            staff_name = (staff.id, staff.username)
            staff_list.append(staff_name)    
    except:
        pass
    staff_id = forms.ChoiceField(label = "Staff", choices=staff_list, widget=forms.Select(attrs={'class':'form-control'}))  
    
class EditStudentResultForm(forms.Form):
    def __init__ (self, *args, **kwargs):
        self.staff_id=kwargs.pop('staff_id')
        super(EditStudentResultForm, self).__init__(*args, **kwargs)
        subject_list = []
        try: 
            subjects = Subjects.objects.filter(staff_id=self.staff_id)
            for subject in subjects:
                subject_single = (subject.id, subject.subject_name)
                subject_list.append(subject_single)
        except:
            subject_list = []
        
        self.fields['subject_id'].choices = subject_list

    session_list = []
    try: 
        sessions = SessionYear.objects.all()
        for session in sessions:
            session_single = (session.id, str(session.session_start_year)+" - "+str(session.session_end_year))
            session_list.append(session_single)
    except:
        session_list = []

    subject_id = forms.ChoiceField(label="Subject", widget=forms.Select(attrs={'class':'form-control'}))
    session_ids = forms.ChoiceField(label="Session Year", choices=session_list, widget=forms.Select(attrs={'class':'form-control'}))
    student_ids = ChoiceNoValidation(label="Student", widget=forms.Select(attrs={'class':'form-control'}))
    assignment_marks = forms.CharField(label = "Assignment Score",widget=forms.TextInput(attrs={'class':'form-control'}))
    exam_marks = forms.CharField(label = "Exam Score",widget=forms.TextInput(attrs={'class':'form-control'}))