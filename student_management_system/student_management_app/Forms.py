from django import forms
from django.forms.widgets import TextInput, FileInput
class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    middle_name = forms.CharField(label = "Middle Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label = "Username",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email",max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = "Password",max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
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
    '''class_choice = (
        ('JSS1', 'JSS 1'),
        ('JSS2', 'JSS 2'),        
        ('JSS3', 'JSS 3'),
        ('SSS1', 'SSS 1'),
        ('SSS2', 'SSS 2'),
        ('SSS3', 'SSS 3'),
    )
    classs = forms.ChoiceField(label = "Class",choices=class_choice, widget=forms.Select(attrs={'class':'form-control'}))'''

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
    first_name = forms.CharField(label = "First Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    middle_name = forms.CharField(label = "Middle Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label = "Last Name",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(label = "Username",max_length=50, widget=TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label = "Email",max_length=50, widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label = "Password",max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
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

class AddSubjectForm(forms.Form):
    subject_name = forms.CharField(label = "Subject Name", max_length=100, widget=TextInput(attrs={'class':'form-control'}))
    subject_status_choice = (
        ('General', 'General'),
        ('Elective', 'Elective')        
    )
    subject_status = forms.ChoiceField(label = "Subject Status",choices=subject_status_choice, widget=forms.Select(attrs={'class':'form-control'}))
    class_choice = (
        ('JSS 1', 'JSS 1'),
        ('JSS 2', 'JSS 2'),        
        ('JSS 3', 'JSS 3'),
        ('SSS 1', 'SSS 1'),
        ('SSS 2', 'SSS 2'),
        ('SSS 3', 'SSS 3'),
    )
    classs = forms.ChoiceField(label = "Class",choices=class_choice, widget=forms.Select(attrs={'class':'form-control'}))

class AddSessionForm(forms.Form):
    term_start = forms.DateField(label = "Term Begins", widget=DateInput(attrs={'class':'form-control'}))
    session_start = forms.DateField(label = "Session Begins", widget=DateInput(attrs={'class':'form-control'}))
    term_end = forms.DateField(label = "Term Ends", widget=DateInput(attrs={'class':'form-control'}))
    session_end = forms.DateField(label = "Session Ends", widget=DateInput(attrs={'class':'form-control'}))