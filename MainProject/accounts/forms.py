from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20,widget=forms.PasswordInput(
        attrs={
            'placeholder':'Enter Password',
        }
    ))

class RegisterForm(UserCreationForm):
    confirm_password = forms.CharField(max_length=40,widget=forms.PasswordInput(
           attrs={
        'placeholder':'Enter Password',
    }
    ))
    class Meta:
        model = Contributor
        exclude = ['is_superuser','is_staff']
