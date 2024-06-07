from django import forms
from .models import User
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email address is already in use. Please log in.')
        return email

class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=100, label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")