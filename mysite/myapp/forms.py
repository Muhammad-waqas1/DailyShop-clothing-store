from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

