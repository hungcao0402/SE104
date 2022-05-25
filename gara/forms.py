from django import forms
from django.contrib.auth.models import User
from . import models
import datetime
from .models import KhachHang,Xe,PhieuThuTien

class NhapBienSoThu(forms.Form):
    bienso=forms.ModelChoiceField(queryset=Xe.objects.all().values_list('bienso',flat=True))
class NhapSoTienThu(forms.Form):
    sotienthu=forms.IntegerField()
