from django.shortcuts import render
from . import forms
from .models import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# @login_required(login_url='/view-request')
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
        return HttpResponseRedirect('view-request')
    
    return render(request,'gara/add_request.html',{'enquiry':enquiry})

def view_request(request):
    enquiry=PhieuTiepNhan.objects.all().filter(date=date.today())

 
    return render(request,'gara/view_request.html', {'enquiries': enquiry})

# def tao_bao_cao_ton(request):
#     p = baocaoton()
#     for i in vattuphutung.objects.all():
        # thangtruoc = 
        # tondau=baocaoton.objects.filter(thangtruoc)

        # c = ct_baocaoton
#     
    #  phatsinh = nhapvattuphutung().objects
#     toncuoi=    

def CapNhatThamSo(request):
    # a = forms.CapNhatQuyDinh()
    data = THAMSO.objects.all()

    # if request.method == 'POST':
    #     f = forms.CapNhatQuyDinh()
    #     f.GiaTri = forms.CapNhatQuyDinh(request.POST)
    #     # a = QuyDinhHienHanh.objects.filter(TenThamSo = "So loai vat tu")
    #     a = THAMSO.objects.first()
    #     f.TenThamSo = a.TenThamSo
        # if f.is_valid():
        #     f.save()
        #     return HttpResponse("luu oke")
        # else:
        #     return HttpResponse("ko co validate")

    return render(request, 'gara/cap_nhat_quy_dinh.html',{'data':data})
