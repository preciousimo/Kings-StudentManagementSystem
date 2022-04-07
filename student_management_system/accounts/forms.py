from django import forms
from django.forms.widgets import TextInput

class RegisterAdminForm(forms.Form):
    first_name = forms.CharField(label = "First Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    last_name = forms.CharField(label = "Last Name",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    username = forms.CharField(label = "Username",max_length=50, widget=TextInput(attrs={'class':'form-control','autocomplete':'off'}))
    email = forms.EmailField(label = "Email",max_length=100, widget=forms.EmailInput(attrs={'class':'form-control','autocomplete':'off'}))
    password = forms.CharField(label = "Password",max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = "Retype Password",max_length=50, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    