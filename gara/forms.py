from email.policy import default
from django import forms
from django.contrib.auth.models import User
from pandas import notnull
from . import models
import datetime
from .models import CT_PhieuSuaChua, KhachHang, PhieuSuaChua, TienCong, VatTuPhuTung,Xe,PhieuThuTien

class NhapBienSoThu(forms.Form):
    bienso=forms.ModelChoiceField(queryset=Xe.objects.all())
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
    dongia=forms.IntegerField()
