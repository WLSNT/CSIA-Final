
from cProfile import Profile as Profile_model
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Folder

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile_model
        fields = ['username', 'email' , 'first_name', 'last_name', 'gender', 'bio']
