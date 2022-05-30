from django.shortcuts import render
from . import forms
from .models import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

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
            kh = KhachHang.objects.all().filter(tenkhachhang=enquiry_x.tenchuxe, dienthoai=enquiry_x.dienthoai)[0]
            if not kh:
                kh = KhachHang(tenkhachhang=enquiry_x.tenchuxe, dienthoai=enquiry_x.dienthoai, diachi=enquiry_x.diachi)
                kh.save()
            xe = Xe.objects.all().filter(bienso=enquiry_x.bienso, makhachhang=kh, mahieuxe=enquiry_x.hieuxe)
            if not xe:
                xe = Xe(bienso=enquiry_x.bienso, makhachhang=kh, mahieuxe=enquiry_x.hieuxe)
                xe.save()

        return HttpResponseRedirect('request')
    
    return render(request,'gara/add_request.html',{'enquiry':enquiry})

def view_request(request):
    enquiry=PhieuTiepNhan.objects.all().filter(date=date.today())
    return render(request,'gara/view_request.html', {'enquiries': enquiry})


def view_baocaoton(request):
    form=forms.AskDateForm()

    if request.method == 'POST':
        month = request.POST['month']
        BCT = None
        try:
            BCT = BaoCaoTon.objects.filter(date__year=month.split('-')[0], date__month=month.split('-')[1])
        except:
            return render(request,'gara/date_to_report.html',{'form':form})
        if BCT: 
            enquiry = ct_baocaoton.objects.all().filter(MaBCT=BCT[0].MaBCT).order_by('-MaVTPT_id').reverse()
            return render(request, 'gara/baocaoton.html',  {'enquiries': enquiry, 'month': month})
        else:
            return render(request,'gara/date_to_report.html',{'form':form})

    return render(request,'gara/date_to_report.html',{'form':form})

def save_baocaoton(request):
    now = date.today()
    bct_before = BaoCaoTon.objects.filter(date__year=now.year, 
                    date__month=now.month-1)
    
    BCT = BaoCaoTon(date=date)
    BCT.save()
    vtpt = VatTuPhuTung.objects.all()
    
    if bct_before:
        
        for item in vtpt:
            toncuoi = item.soluong
            try:
                phatsinh = nhapvattuphutung.objects.filter(date__year=now.year, date__month=now.month, mavattuphutrung=item.mavattuphutung)[0].soluong
            except:
                phatsinh = 0
            tondau = bct_before.objects.all().filter(MaVTPT=item.mavattuphutung)[0].TonCuoi
            tempt = ct_baocaoton(MaBCT=BCT, MaVTPT=item, TonDau=tondau, TonCuoi=toncuoi, PhatSinh=phatsinh)
            tempt.save()
    else:
        for item in vtpt:
            toncuoi = item.soluong
            try:
                phatsinh = nhapvattuphutung.objects.filter(date__year=now.year, date__month=now.month, mavattuphutrung=item.mavattuphutung)[0].soluong
            except:
                phatsinh = 0
            tondau = 0
            tempt = ct_baocaoton(MaBCT=BCT, MaVTPT=item, TonDau=tondau, TonCuoi=toncuoi, PhatSinh=phatsinh)
            tempt.save()
    
    enquiry = ct_baocaoton.objects.all().filter(MaBCT=BCT).order_by('-MaVTPT_id').reverse()
    return render(request, 'gara/baocaoton.html',  {'enquiries': enquiry, 'month': now})

def baocaoton_luachon(request):
    return render(request, 'gara/baocaoton_luachon.html')