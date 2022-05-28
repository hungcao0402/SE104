from imp import C_BUILTIN
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from .models import *
from datetime import date
# from django.contrib.auth.decorators import login_required

def nhapbienso_phieuthu(request):
    enquiry=forms.NhapBienSoThu
    if request.method=='POST':
        enquiry=forms.NhapBienSoThu(request.POST)
        print('POST is method')
        if enquiry.is_valid():
            print('enquiry is valid')
            print(request.POST['bienso'])
            xe_x=Xe.objects.get(maxe=request.POST['bienso']) 
            return redirect(f'dien_phieuthu/{xe_x.maxe}')
    context= {'enquiry':enquiry}        
    return render(request,'phieu thu tien/nhapbienso_phieuthu.html',context)

def xacnhan_phieuthu(request,maxe):
    nhapsotienthu=forms.NhapSoTienThu
    xe_x=Xe.objects.get(maxe=maxe)
    khach_x=KhachHang.objects.get(makhachhang=xe_x.makhachhang_id)
    context= {'nhapsotienthu':nhapsotienthu,'xe_x': xe_x,'khach_x':khach_x} 
    if request.method=='POST':
        nhapsotienthu=forms.NhapSoTienThu(request.POST)  
        if nhapsotienthu.is_valid():
            print('enquiry is valid')
            tienthu=nhapsotienthu.cleaned_data['sotienthu']
            if tienthu<xe_x.tienno:
                print('chua hoan thanh')
                return render(request,'phieu thu tien/nhapsotienthu.html',context)   
            else: 
                phieuthutien_x=PhieuThuTien.objects.create(maxe_id=xe_x.maxe,sotienthu=tienthu)
                xe_x.tienno=0
                xe_x.save()
                print('da luu vao database')
    return render(request,'phieu thu tien/nhapsotienthu.html',context)       
def view_phieuthu(request,maphieuthutien):
    phieuthu=PhieuThuTien.objects.get(maphieuthutien=maphieuthutien)
    xe_x=Xe.objects.get(maxe=phieuthu.maxe)
    context={'xe_x':xe_x,'phieuthu':phieuthu}
    return render(request,'phieu thu tien/view_phieuthu.html',context)       

def nhapbiensosua(request):
    enquiry=forms.NhapBienSoSua
    if request.method=='POST':
        enquiry=forms.NhapBienSoSua(request.POST)
        print(request.POST['bienso'])
        xe_x=Xe.objects.get(bienso=request.POST['bienso'])
        phieusua_x=PhieuSuaChua.objects.create(maxe_id=xe_x.maxe,tongthanhtien=0)
        phieusua_x.save()
        return redirect(f'view_phieusua/{phieusua_x.maphieusuachua}')
    return render(request,'phieusuachua/nhapbiensosua.html', {'enquiry':enquiry}) 
def view_phieusua(request ,maphieusuachua):
    phieusua=PhieuSuaChua.objects.get(maphieusuachua=maphieusuachua)
    xe_x=Xe.objects.get(maxe=phieusua.maxe_id)
    data=CT_PhieuSuaChua.objects.all().filter(maphieusuachua=maphieusuachua)
    enquiry=forms.NhapCTSuaChua
    context= {'phieusua':phieusua,'xe_x':xe_x,'data':data,'enquiry':enquiry}
    if request.method=='POST':
        print('request method la POST')
        enquiry=forms.NhapCTSuaChua(request.POST)
        if enquiry.is_valid():
            print('enquiry is valid')
            tiencong_x=TienCong.objects.get(loaitiencong=enquiry.cleaned_data['loaitiencong'])
            tongtiencong=tiencong_x.tiencong*enquiry.cleaned_data['solan']
            phieusua_x=CT_PhieuSuaChua.objects.create(maphieusuachua_id=maphieusuachua,
            matiencong_id=tiencong_x.matiencong,tiencong=tongtiencong,
            solan=enquiry.cleaned_data['solan'], noidung=enquiry.cleaned_data['noidung'],tongtien=tongtiencong)
            tongthanhtien_x=phieusua.tongthanhtien+tongtiencong
            phieusua.tongthanhtien=tongthanhtien_x
            return render(request,'phieusuachua/view_phieusua.html',context ) 

    # context={'enquiry':enquiry}
    
    # form_chitiet=forms.
    return render(request,'phieusuachua/view_phieusua.html',context ) 

def view_ctphieusuachua(request,mact_phieusuachua):
    ct_phieusua=CT_PhieuSuaChua.objects.get(mact_phieusuachua=mact_phieusuachua)  
    data=CT_VatTuPhuTung.objects.all().filter(mact_phieusuachua=mact_phieusuachua)
    nhap_ctvtpt=forms.NhapCT_VatTuPhuTung
    context={'ct_phieusua':ct_phieusua,'nhap_ctvtpt':nhap_ctvtpt,'data':data}
    # context={'nhap_ctvtpt':nhap_ctvtpt}
    if request.method=='POST':
        print('request method is POST')
        nhap_ctvtpt=forms.NhapCT_VatTuPhuTung(request.POST)
        if nhap_ctvtpt.is_valid():  
                print('phieu nhap is valid')
                tien1_ctvattu=nhap_ctvtpt.cleaned_data['dongia']*nhap_ctvtpt.cleaned_data['soluong']
                print(nhap_ctvtpt.cleaned_data['dongia'],'...',nhap_ctvtpt.cleaned_data['soluong'])
                vattu_x=VatTuPhuTung.objects.get(tenvattuphutung=nhap_ctvtpt.cleaned_data['tenvattuphutung'])
                CT_VatTuPhuTung.objects.create(mact_phieusuachua_id=mact_phieusuachua,
                mavattuphutung_id=vattu_x.mavattuphutung, soluong=nhap_ctvtpt.cleaned_data['soluong'],
                dongia=nhap_ctvtpt.cleaned_data['dongia'], tongthanhtien=tien1_ctvattu)
                tong_tatcavattu=tien1_ctvattu+ct_phieusua.tongtienvattu
                ct_phieusua.tongtienvattu=tong_tatcavattu
                tongtien_1ctsc=tong_tatcavattu+ct_phieusua.tiencong
                ct_phieusua.tongtien=tongtien_1ctsc
                ct_phieusua.save()
                phieusua_x=PhieuSuaChua.objects.get(maphieusuachua=ct_phieusua.maphieusuachua_id)
                tong_phieusua=phieusua_x.tongthanhtien + tongtien_1ctsc
                phieusua_x.tongthanhtien=tong_phieusua
                phieusua_x.save()                              
    return render(request,'phieusuachua/view_ctphieusua.html',context ) 

