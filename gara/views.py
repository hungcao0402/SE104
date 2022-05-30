from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from .models import *
from datetime import date
import datetime
from django.urls import reverse


def phieunhapvtpt(request):
    # Bước 0 : Xác nhận có tạo phiếu nhập hay không ?
    if request.method=='POST':
        # Tạo phiếu nhập với khởi tạo tổng tiền bằng 0
        phieunhap_x=PhieuNhapVTPT.objects.create(tongtien=0)
        # Đi đến trang view_ctphieunhapvtpt
        return redirect('gara:view_ctphieunhapvtpt')
    return render(request,'phieunhapvtpt/xacnhannhap.html')

def view_ctphieunhapvtpt(request):
    enquiry=forms.NhapCTVatTuPhuTung
    if request.method=='POST':
        enquiry=forms.NhapCTVatTuPhuTung(request.POST)
        print("-----------------")
        if enquiry.is_valid():
            # Bước 1: Kiểm tra tên phụ tùng đã có tồn tại hay chưa, chưa thì khởi tạo
            print("Bước 1")
            # Bước 2: Lưu dữ liệu
            # Lấy mã phiếu nhập vừa được tạo  
            maphieunhapvtpt_x=PhieuNhapVTPT.objects.order_by('-maphieunhapvtpt').values_list('maphieunhapvtpt', flat=True)
            # Lấy phiếu nhập vừa được tạo
            phieunhapvtpt_last=PhieuNhapVTPT.objects.latest('maphieunhapvtpt')
            # Lấy dữ liệu phụ tùng có mã phụ tùng nhập vào
            phutung_x=VatTuPhuTung.objects.get(mavattuphutung=request.POST['mavattuphutung'])
            print("Mavattuphutung :",phutung_x.mavattuphutung)
            # Lưu dữ liệu chia tiết phiếu nhập
            ctphieunhapvtpt_x=CT_PhieuNhapVTPT.objects.create(mavattuphutung_id=phutung_x.mavattuphutung,maphieunhapvtpt_id=maphieunhapvtpt_x[0],soluong=enquiry.cleaned_data['soluong'],dongia=enquiry.cleaned_data['dongia'])
            # Cập nhật lại tổng tiền cho phiếu nhập (ban đầu gán là 0)
            phieunhapvtpt_last.tongtien= enquiry.cleaned_data['soluong']*enquiry.cleaned_data['dongia']
            # Lưu lại cập nhật
            phieunhapvtpt_last.save()
            # Chuyển đến trang hiển thị
            print("Hiển thị kết quả")
            return redirect(f'view_cappnhatvtpt/{phutung_x.mavattuphutung}')
    return render(request,'phieunhapvtpt/nhapphutung.html',{'enquiry':enquiry})

def view_cappnhatvtpt(request,mavattuphutung):
    print("---------------")
    slnhap_ctvtpt=CT_PhieuNhapVTPT.objects.filter(mavattuphutung=mavattuphutung).order_by('-mact_phieunhapvtpt').values_list('soluong', flat=True)[:1]
    phutung_=VatTuPhuTung.objects.get(mavattuphutung=mavattuphutung)
    print(phutung_.soluong)
    phutung_.soluong +=  slnhap_ctvtpt[0]
    print(phutung_.soluong)
    phutung_.save()
    ctvtpt=CT_PhieuNhapVTPT.objects.latest('-mact_phieunhapvtpt')
    context={'ctvtpt':ctvtpt,'capnhatphutung':phutung_}
    return render(request,'phieunhapvtpt/capnhatphutung.html',context)
 
