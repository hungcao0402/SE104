from django import forms
from django.contrib.auth.models import User
from .models import *
import datetime
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

class TiepNhanForm(forms.ModelForm):
    class Meta:
        model= PhieuTiepNhan
        fields=['tenchuxe','bienso','hieuxe','dienthoai','diachi']

# class CustomerUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }
#         fields= '__all__'

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model=models.Customer
#         fields=['address','mobile','profile_pic']
#         fields= '__all__'

class RegisterForm(forms.ModelForm):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    mobile = forms.CharField(max_length=10)
    username = forms.CharField(max_length=20)
    address = forms.CharField(max_length=100)
    password = forms.CharField(max_length=12)
    emails = forms.EmailField(max_length=90)
    profile_pic = forms.ImageField()
    class Meta:
        model= Customer
        fields=['username','firstname','lastname','emails','password','mobile', 'address']
        widgets = {
            'password': forms.PasswordInput()
        }
class CustomerUpdateForm(UserChangeForm):
    emails = forms.CharField(max_length=90)
    class Meta:
        model = Customer
        fields= ['profile_pic','firstname','lastname','emails','mobile','address']
        # fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
class CustomerUpdateAccount(UserChangeForm):
    password = forms.CharField(max_length=20)
    class Meta:
        model = Customer
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput()
        }
    