from django.shortcuts import render
from . import forms
from .models import *
from datetime import date
# Create your views here.

def tiep_nhan(request):
    enquiry=forms.TiepNhanForm()
    count = PhieuTiepNhan.objects.filter(date=date.today()).count()
    if count > 30: ##Cần sửa với tham số
        enquiries=PhieuTiepNhan.objects.all().filter(date=date.today())

        return render(request, 'gara/view_request.html', {'enquiries': enquiries})

    if request.method=='POST':
        enquiry=forms.TiepNhanForm(request.POST)
        if enquiry.is_valid():
            enquiry_x=enquiry.save()
        return render(request, 'gara/view_request.html', {'enquiries': enquiries})
    
    return render(request,'gara/add_request.html',{'enquiry':enquiry})

def view_request(request):
    enquiries=PhieuTiepNhan.objects.all().filter(date=date.today())
    return render(request,'gara/view_request.html', {'enquiries': enquiries})
