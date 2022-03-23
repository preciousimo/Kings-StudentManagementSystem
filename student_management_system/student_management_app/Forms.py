from django import forms
from django.forms.widgets import TextInput, FileInput
from student_management_app.models import SessionYear
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
    term_start = forms.DateField(label = "Term Starts", widget=DateInput(attrs={'class':'form-control'}))
    session_start = forms.DateField(label = "Session Starts", widget=DateInput(attrs={'class':'form-control'}))
    term_end = forms.DateField(label = "Term Ends", widget=DateInput(attrs={'class':'form-control'}))
    session_end = forms.DateField(label = "Session Ends", widget=DateInput(attrs={'class':'form-control'}))

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
    profile_picture = forms.FileField(label = "Profile Picture",max_length=50, widget=FileInput(attrs={'class':'form-control'}))
    curriculum_vitae = forms.FileField(label = "Curriculum Vitae",max_length=50, widget=FileInput(attrs={'class':'form-control'}))
    address = forms.CharField(label = "Address",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    state = forms.CharField(label = "State",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    nationality = forms.CharField(label = "Nationality", max_length=50, widget=TextInput(attrs={'class':'form-control'}))


    session_start = forms.DateField(label = "Session Start", widget=DateInput(attrs={'class':'form-control'}))
    session_end = forms.DateField(label = "Session End", widget=DateInput(attrs={'class':'form-control'}))