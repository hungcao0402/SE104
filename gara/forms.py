from django import forms
from django.contrib.auth.models import User
from .models import *
import datetime
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm

# class TiepNhanForm(forms.ModelForm):
#     class Meta:
#         model= PhieuTiepNhan
#         fields=['tenchuxe','bienso','hieuxe','dienthoai','diachi']

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
#         model=models.Staff
#         fields=['address','mobile','profile_pic']
#         fields= '__all__'

#Phan cua Chau Tan -20520926
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
        model= Staff
        fields=['username','firstname','lastname','emails','password','mobile', 'address','profile_pic']
        widgets = {
            'password': forms.PasswordInput()
        }
class StaffUpdateForm(UserChangeForm):
    emails = forms.CharField(max_length=90)
    class Meta:
        model = Staff
        fields= ['profile_pic','firstname','lastname','emails','mobile','address']
        # fields = '__all__'
        widgets = {
            'password': forms.PasswordInput()
        }
class StaffUpdateAccount(UserChangeForm):
    password = forms.CharField(max_length=20)
    class Meta:
        model = Staff
        fields = ['username','password']
        widgets = {
            'password': forms.PasswordInput()
        }
# Phan cua Ngo Duc Vu -20520950
class NhapBienSoThu(forms.Form):
    bienso=forms.ModelChoiceField(queryset=Xe.objects.filter(tienno__gt=0))
class NhapSoTienThu(forms.Form):
    sotienthu=forms.IntegerField()
class NhapBienSoSua(forms.Form):
    bienso=forms.ModelChoiceField(queryset=Xe.objects.all().values_list('bienso',flat=True))
class NhapCTSuaChua(forms.Form):
    # maphieusuachua=forms.ModelChoiceField(queryset=PhieuSuaChua.objects.all())
    solan=forms.IntegerField()
    loaitiencong=forms.ModelChoiceField(queryset=TienCong.objects.all())
    # tiencong=forms.IntegerField()
    noidung=forms.CharField(max_length=100)
    # tongtien=forms.IntegerField()
class NhapCT_VatTuPhuTung(forms.Form):
    tenvattuphutung=forms.ModelChoiceField(queryset=VatTuPhuTung.objects.all())   #.values_list('tenvattuphutung',flat=True))
    soluong=forms.IntegerField()

# Phan cua Cao Van Hung


class TiepNhanForm(forms.ModelForm):
    class Meta:
        model=PhieuTiepNhan
        fields=['tenchuxe','bienso','hieuxe','dienthoai','diachi']

class AskDateForm(forms.Form):
    date=forms.DateField(widget=forms.SelectDateWidget())

# Phan cua Nguyen Tri

class CapNhatQuyDinh(forms.ModelForm):
    class Meta:
        # def __init__(self):
        #     print("in init")
        model = QuyDinhHienHanh
        fields = ['MaThamSo','TenThamSo','GiaTri']
        widgets = {
            'GiaTri': forms.TextInput(attrs={'class':'form_GiaTri'}),
            'TenThamSo': forms.TextInput(attrs={'class':'form_TenThamSo'})
        }

class NhapCTVatTuPhuTung(forms.ModelForm):
    class Meta:
        model = VatTuPhuTung
        fields = ['tenvattuphutung','soluong','dongia']
     
class ThemHieuXe(forms.Form):
        tenhieuxe = forms.CharField(max_length=50)
class ThemTienCong(forms.Form):
    loaitiencong = forms.CharField(max_length=100)
    tiencong = forms.IntegerField(min_value=0)