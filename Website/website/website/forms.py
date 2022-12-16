from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'type':'password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'type':'password'}))
    
    class Meta:
        model = User


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = {'username', 'email', 'password1', 'password2'}
