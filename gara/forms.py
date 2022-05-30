from django import forms
from django.contrib.auth.models import User
from . import models
import datetime
from .models import KhachHang,Xe,PhieuThuTien

class NhapBienSoThu(forms.Form):
    bienso=forms.ModelChoiceField(queryset=Xe.objects.all().values_list('bienso',flat=True))
class NhapSoTienThu(forms.Form):
    sotienthu=forms.IntegerField()


# =========================================================
# NGUYEN TRI

class CapNhatQuyDinh(forms.ModelForm):
    class Meta:
        # def __init__(self):
        #     print("in init")
        model = models.QuyDinhHienHanh
        fields = ['MaThamSo','TenThamSo','GiaTri']
        widgets = {
            'GiaTri': forms.TextInput(attrs={'class':'form_GiaTri'}),
            'TenThamSo': forms.TextInput(attrs={'class':'form_TenThamSo'})
        }