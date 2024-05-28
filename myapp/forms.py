from django.forms import ModelForm
from .models import Expense
from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class ExpenseForm(ModelForm):
    class Meta:
        model = Expense
        fields = ('name','amount','category')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=60,widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']