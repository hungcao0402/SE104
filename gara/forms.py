from django import forms
from django.contrib.auth.models import User
from . import models
import datetime

class TiepNhanForm(forms.ModelForm):
    class Meta:
        model=models.PhieuTiepNhan
        fields=['tenchuxe','bienso','hieuxe','dienthoai','diachi']

class CapNhatQuyDinh(forms.ModelForm):
    class Meta:
        # def __init__(self):
        #     print("in init")
        model = models.THAMSO
        fields = ['TenThamSo','GiaTri']
        widgets = {
            'GiaTri': forms.TextInput(attrs={'class':'form_GiaTri'})
        }
    
