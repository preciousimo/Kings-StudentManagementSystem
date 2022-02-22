from django import forms

class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=50)
    middle_name = forms.CharField(label = "Middle Name",max_length=50)
    last_name = forms.CharField(label = "Last Name",max_length=50)
    username = forms.CharField(label = "Username",max_length=50)
    email = forms.EmailField(label = "Email",max_length=50, widget=forms.EmailInput())
    password = forms.CharField(label = "Password",max_length=50, widget=forms.PasswordInput())
    date_of_birth = forms.DateField(widget=DateInput())
    phone_number = forms.CharField(label = "Phone Number",max_length=50)
    gender = forms.CharField(label = "Gender",max_length=50)
    profile_picture = forms.FileField(label = "Profile Picture",max_length=50)
    address = forms.CharField(label = "Address",max_length=50)
    state = forms.CharField(label = "State",max_length=50)
    nationality = forms.CharField(label = "Nationality",max_length=50)
    term_start = forms.DateField(label = "Term Begins", widget=DateInput())
    term_end = forms.DateField(label = "Term Ends", widget=DateInput())
    session_start = forms.DateField(label = "Session Begins", widget=DateInput())
    session_end = forms.DateField(label = "Session Ends", widget=DateInput())