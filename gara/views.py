from http.server import ThreadingHTTPServer
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
    list_phieusua=PhieuSuaChua.objects.all().filter(maxe_id=xe_x.maxe)

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
                for i in list_phieusua:
                    i.tinhtrangthutien=1
                    i.save()
    context= {'nhapsotienthu':nhapsotienthu,'xe_x': xe_x,'khach_x':khach_x, 'data':list_phieusua} 
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
            phieusua.save()
            #cap nhat tien no xe
            xe_x=Xe.objects.get(maxe=phieusua.maxe_id)
            tienno_xe=xe_x.tienno+tongtiencong
            xe_x.tienno=tienno_xe
            xe_x.save()
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
                ct_phieusua.tongtien=tong_tatcavattu+ct_phieusua.tiencong
                ct_phieusua.save()
                phieusua_x=PhieuSuaChua.objects.get(maphieusuachua=ct_phieusua.maphieusuachua_id)
                tong_phieusua=phieusua_x.tongthanhtien + tien1_ctvattu
                phieusua_x.tongthanhtien=tong_phieusua
                phieusua_x.save()
                            #cap nhat tien no xe
                xe_x=Xe.objects.get(maxe=phieusua_x.maxe_id)
                tienno_xe=xe_x.tienno+tien1_ctvattu
                xe_x.tienno=tienno_xe
                xe_x.save()
                # capnhattienno(phieusua_x.maphieusuachua,tong_phieusua)                         
    return render(request,'phieusuachua/view_ctphieusua.html',context)

def delete_ctphieusua(request,mact_phieusuachua):
    ctphieusua=CT_PhieuSuaChua.objects.get(mact_phieusuachua=mact_phieusuachua)
    phieusua_x=PhieuSuaChua.objects.get(maphieusuachua=ctphieusua.maphieusuachua_id)
    print(phieusua_x.tongthanhtien,'-',ctphieusua.tongtien)
    tongthanhtien_x=phieusua_x.tongthanhtien-ctphieusua.tongtien
    phieusua_x.tongthanhtien=tongthanhtien_x
    print(phieusua_x.tongthanhtien)
                                #cap nhat tien no xe
    xe_x=Xe.objects.get(maxe=phieusua_x.maxe_id)
    tienno_xe=xe_x.tienno-ctphieusua.tongtien
    xe_x.tienno=tienno_xe
    xe_x.save()
    phieusua_x.save()
    ctphieusua.delete()
    maphieusuachua_x=int(phieusua_x.maphieusuachua)
    return redirect(f'/view_phieusua/{maphieusuachua_x}')
def delete_chitietvattu(request,mact_vattuphutung,mact_phieusuachua,maphieusuachua):
    ctvt=CT_VatTuPhuTung.objects.get(mact_vattuphutung=mact_vattuphutung)
    ctphieusua=CT_PhieuSuaChua.objects.get(mact_phieusuachua=mact_phieusuachua)
    phieusua_x=PhieuSuaChua.objects.get(maphieusuachua=maphieusuachua)
    tien_1vattu=ctvt.soluong*ctvt.dongia
    tongtien=ctphieusua.tongtien-tien_1vattu
    tongtienvattu_x=ctphieusua.tongtienvattu-tien_1vattu
    ctphieusua.tongtienvattu=tongtienvattu_x
    ctphieusua.tongtien=tongtien
    print(phieusua_x.tongthanhtien,'-',tien_1vattu)
    tongthanhtien_x=phieusua_x.tongthanhtien-tien_1vattu
    print(tongthanhtien_x)
    phieusua_x.tongthanhtien=tongthanhtien_x
                                    #cap nhat tien no xe
    xe_x=Xe.objects.get(maxe=phieusua_x.maxe_id)
    tienno_xe=xe_x.tienno-tien_1vattu
    xe_x.tienno=tienno_xe
    xe_x.save()
    ctphieusua.save()
    phieusua_x.save()
    ctvt.delete()
    return redirect(f'/view_ctphieusua/{mact_phieusuachua}')




    
# def re_calculate(maphieusuachua):
# def re_calculate_sum(maphieusuachua):
#     phieusua=PhieuSuaChua.objects.get()

# def capnhattienno(maphieusuachua,tongthanhtien):
#     print('bat dau ham cap nhat tien no')
#     phieusua=PhieuSuaChua.objects.get(maphieusuachua=maphieusuachua)
#     print(phieusua.maphieusuachua)
#     xe_x=Xe.objects.get(maxe=phieusua.maxe_id)
#     xe_x.tienno=tongthanhtien
#     xe_x.save()
