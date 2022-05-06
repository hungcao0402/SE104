from django.shortcuts import render
from . import forms
from .models import *
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required(login_url='/view-request')
def tiep_nhan(request):
    enquiry=forms.TiepNhanForm()
    count = PhieuTiepNhan.objects.filter(date=date.today()).count()
    if count > 30: ##Cần sửa với tham số
        enquiries=PhieuTiepNhan.objects.all().filter(date=date.today())

        return render(request, 'gara/view_request.html', {'enquiries': enquiries})

    if request.method=='POST':
        enqouiry=forms.TiepNhanForm(request.POST)
        if enquiry.is_valid():
            enquiry_x=enquiry.save()
        return render(request, 'gara/view_request.html', {'enquiries': enquiries})
    
    return render(request,'gara/add_request.html',{'enquiry':enquiry})

def view_request(request):
    enquiries=PhieuTiepNhan.objects.all().filter(date=date.today())
    return render(request,'gara/view_request.html', {'enquiries': enquiries})

def tao_bao_cao_ton(request):
    p = baocaoton()
    for i in vattuphutung.objects.all():
        # thangtruoc = 
        # tondau=baocaoton.objects.filter(thangtruoc)

        c = ct_baocaoton
#     
    #  phatsinh = nhapvattuphutung().objects
#     toncuoi=    