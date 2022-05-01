from django import forms
from django.contrib.auth.models import User
from . import models

class TiepNhanForm(forms.ModelForm):
    class Meta:
        model=models.PhieuTiepNhan
        fields=['tenchuxe','bienso','hieuxe','dienthoai','diachi']
    