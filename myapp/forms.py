from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CreateImage(forms.ModelForm):
    class Meta:
        model = models.Image
        fields = ['image']


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'mobile_number', 'address', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
