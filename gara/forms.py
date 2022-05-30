
from django import forms
from django.contrib.auth.models import User
from . import models
import datetime
from .models import VatTuPhuTung, CT_VatTuPhuTung, CT_PhieuNhapVTPT

class NhapCTVatTuPhuTung(forms.Form):
    mavattuphutung=forms.ModelChoiceField(queryset=VatTuPhuTung.objects.all()) 
    #tenvattuphutung=forms.ModelChoiceField(queryset=VatTuPhuTung.objects.all())   #.values_list('tenvattuphutung',flat=True))
    soluong=forms.IntegerField()
    dongia=forms.IntegerField()
