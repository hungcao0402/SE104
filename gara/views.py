from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from .models import *
from datetime import date
# from django.contrib.auth.decorators import login_required

def tao_form(request):
    enquiry=forms.NhapBienSoThu
    if request.method=='POST':
        enquiry=forms.NhapBienSoThu(request.POST)
        print(request.POST['bienso'])
        xe_x=Xe.objects.get(bienso=request.POST['bienso']) 
        return redirect(f'dien_phieuthu/{xe_x.maxe}')
    return render(request,'gara/nhapbienso_phieuthu.html', {'enquiry':enquiry})

def xacnhan_phieuthu(request,maxe):
    nhapsotienthu=forms.NhapSoTienThu
    xe_x=Xe.objects.get(maxe=maxe)
    khach_x=KhachHang.objects.get(makhachhang=xe_x.makhachhang_id)
    context= {'nhapsotienthu':nhapsotienthu,'xe_x': xe_x,'khach_x':khach_x} 
    if request.method=='POST':
        nhapsotienthu=forms.NhapSoTienThu(request.POST)  
        if nhapsotienthu.is_valid():
            tienthu=nhapsotienthu.cleaned_data['sotienthu']
            if tienthu<xe_x.tienno:
                print('chua hoan thanh')
                return render(request,'gara/nhapsotienthu.html',context)   
            else: 
                phieuthutien_x=PhieuThuTien
                print('helllllooo',phieuthutien_x.maxe)
                phieuthutien_x=PhieuThuTien.objects.create(maxe_id=xe_x.maxe,sotienthu=tienthu)
                phieuthutien_x.save()
                xe_x.tienno=0
                xe_x.save()
                print('da luu vao database')
    return render(request,'gara/nhapsotienthu.html',context)       
def view_phieuthu(request,maphieuthutien):
    phieuthu=PhieuThuTien.objects.get(maphieuthutien=maphieuthutien)
    xe_x=Xe.objects.get(maxe=phieuthu.maxe)
    context={'xe_x':xe_x,'phieuthu':phieuthu}
    return render(request,'gara/view_phieuthu.html',context)           
