from decimal import MAX_EMAX
import http
from itertools import count
from multiprocessing import context
from cv2 import DFT_COMPLEX_INPUT
from django.http import HttpResponse
from django.shortcuts import render,redirect
from numpy import dsplit
from . import forms
from .models import *
from datetime import date
# from django.contrib.auth.decorators import login_required

from django.db.models import Sum, Count
import pandas as pd


def nhapbienso_phieuthu(request):
    enquiry=forms.NhapBienSoThu
    if request.method=='POST':
        enquiry=forms.NhapBienSoThu(request.POST)
        print(request.POST['bienso'])
        xe_x=Xe.objects.get(bienso=request.POST['bienso']) 
        return redirect(f'dien_phieuthu/{xe_x.maxe}')
    return render(request,'phieu thu tien/nhapbienso_phieuthu.html', {'enquiry':enquiry})

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
                return render(request,'phieu thu tien/nhapsotienthu.html',context)   
            else: 
                phieuthutien_x=PhieuThuTien
                print('helllllooo',phieuthutien_x.maxe)
                phieuthutien_x=PhieuThuTien.objects.create(maxe_id=xe_x.maxe,sotienthu=tienthu)
                phieuthutien_x.save()
                xe_x.tienno=0
                xe_x.save()
                print('da luu vao database')
    return render(request,'phieu thu tien/nhapsotienthu.html',context)       
def view_phieuthu(request,maphieuthutien):
    phieuthu=PhieuThuTien.objects.get(maphieuthutien=maphieuthutien)
    xe_x=Xe.objects.get(maxe=phieuthu.maxe)
    context={'xe_x':xe_x,'phieuthu':phieuthu}
    return render(request,'phieu thu tien/view_phieuthu.html',context)       

def tao_form(request):
    enquiry=forms.NhapBienSoThu
    if request.method=='POST':
        enquiry=forms.NhapBienSoThu(request.POST)
        print(request.POST['bienso'])
        xe_x=Xe.objects.get(bienso=request.POST['bienso']) 
        return redirect(f'dien_phieuthu/{xe_x.maxe}')
    return render(request,'phieu thu tien/nhapbienso_phieuthu.html', {'enquiry':enquiry})    


# ======================================================================
# NGUYEN TRI
# QUY DINH

def update_default():
    QuyDinhHienHanh.objects.create(TenThamSo="So hieu xe", GiaTri = 0)
    QuyDinhHienHanh.objects.create(TenThamSo="So xe sua chua toi da", GiaTri = 0)
    QuyDinhHienHanh.objects.create(TenThamSo="So loai vat tu", GiaTri = 0)
    QuyDinhHienHanh.objects.create(TenThamSo="So loai tien cong", GiaTri = 0)

def regular_update(request):
    # enquiries = QuyDinhHienHanh.objects.all().filter()
    a = forms.CapNhatQuyDinh()
    if QuyDinhHienHanh.objects.all().exists() ==False:
        update_default()
    data = QuyDinhHienHanh.objects.all()
    return render(request, 'gara/cap_nhat_quy_dinh.html',{'fa': a,'data':data})


def save_regular_update(request):
    if request.method == 'POST':
        f = forms.CapNhatQuyDinh(request.POST)
        # a = QuyDinhHienHanh.objects.first()
        if f.is_valid():
            f.save()
            return redirect('/')
        else:
            return HttpResponse("ko co validate")
    else:
        return HttpResponse("not POST request")


def delete_QuyDinh(self):
    QuyDinhHienHanh.objects.all().delete()


def update_quydinh(request , mts):
    quy_dinh = QuyDinhHienHanh.objects.get(MaThamSo=mts)
    form = forms.CapNhatQuyDinh(instance= quy_dinh)

    if request.method == 'POST':
        form = forms.CapNhatQuyDinh(request.POST, instance= quy_dinh)
        if form.is_valid():
            form.save()
            return redirect('/thamso')
    context = {'form':form}
    return render(request, 'gara/update_form_qd.html',{'form': form})
    # return render(request, 'gara/update_form.html', context)

def delete_quydinh(request, mts):
    quy_dinh = QuyDinhHienHanh.objects.get(MaThamSo=mts)
    if request.method == "POST":
        quy_dinh.delete()
        return redirect('/thamso')
    context = {'item': quy_dinh}
    return render(request, 'gara/delete_qd.html', context)

# ======================================================================
# NGUYEN TRI
# DOANH SO

# def add_ctBaoCaoDoanhSO(request):
    # psc_xe = PhieuSuaChua.objects.select_related("maxe__mahieuxe").all()
    # hieuxe = HieuXe.objects.all()
    # psc_xe.select_related("mahieuxe")
    # # maxe_luotsua_thanhtien = psc_xe.values("maxe").annotate(count=Count("maxe")).annotate(Sum=Sum("tongthanhtien"))
    # b = psc_xe.values("maxe").annotate(count=Count("maxe")).annotate(Sum=Sum("tongthanhtien"))
    # a = hieuxe.values("tenhieuxe","hieuxe")
    # for i in range(len(a)):
    #     print(a[i]['tenhieuxe'], a[i]['hieuxe'])
    #     sum_hx = 0
    #     count_hx = 0
    #     for j in range(len(b)):
    #         if a[i]['hieuxe'] == b[j]["maxe"]:
    #             sum_hx += b[j]["Sum"]
    #             count_hx += b[j]["Sum"]
    #     CT_BaoCaoDoanhSO.objects.create(mahieuxe= a[i]['hieuxe'], luotsua=sum_hx,thanhtien=count_hx)
#     return 0

def data_xe_hieuxe_psc():
    x = Xe.objects.all()
    hx = HieuXe.objects.all()
    psc = PhieuSuaChua.objects.all()
    df_x = pd.DataFrame(x.values())
    df_hx = pd.DataFrame(hx.values())
    df_psc = pd.DataFrame(psc.values())
    df_xhx = df_x.join(df_hx.set_index("mahieuxe"), on = "mahieuxe_id")
    df = df_psc.join(df_xhx.set_index("maxe"), on = "maxe_id")

    # df['ngaytiepnhan'] = pd.to_datetime(df['ngaytiepnhan'])
    # df['ngaytiepnhan'].dt.to_period('M')

    df['ngaylapphieu'] = pd.to_datetime(df['ngaylapphieu'])
    df['thanglapphieu']=df['ngaylapphieu'].dt.to_period('M')
    df['month'] = df['ngaylapphieu'].dt.month
    df['year'] = df['ngaylapphieu'].dt.year


    ct_ds = df.groupby(["month","year","tenhieuxe"])['tongthanhtien'].agg(['sum','count']).reset_index()
    total = df.groupby(["month","year"])['tongthanhtien'].agg(['sum','count']).reset_index()
    data = pd.merge(ct_ds,total, how="left", on=['month','year']) #col: ['month', 'year', 'tenhieuxe', 'sum', 'count_x', 'count_y'],
    data['tile']=data['count_x']/data['count_y']*100
    return data

def Bao_Cao_Doanh_So(request):
    CT_BaoCaoDoanhSO.objects.all().delete()
    BaoCaoDoanhSo.objects.all().delete()
    x = Xe.objects.all()
    hx = HieuXe.objects.all()
    psc = PhieuSuaChua.objects.all()
    df_x = pd.DataFrame(x.values())
    df_hx = pd.DataFrame(hx.values())
    df_psc = pd.DataFrame(psc.values())
    df_xhx = df_x.join(df_hx.set_index("mahieuxe"), on = "mahieuxe_id")
    df = df_psc.join(df_xhx.set_index("maxe"), on = "maxe_id")

    # df['ngaytiepnhan'] = pd.to_datetime(df['ngaytiepnhan'])
    # df['ngaytiepnhan'].dt.to_period('M')

    df['ngaylapphieu'] = pd.to_datetime(df['ngaylapphieu'])
    df['thanglapphieu']=df['ngaylapphieu'].dt.to_period('M')
    df['month'] = df['ngaylapphieu'].dt.month
    df['year'] = df['ngaylapphieu'].dt.year

    ct_ds = df.groupby(["month","year","tenhieuxe"])['tongthanhtien'].agg(['sum','count']).reset_index()
    total = df.groupby(["month","year"])['tongthanhtien'].agg(['sum','count']).reset_index()
    data = pd.merge(ct_ds,total, how="left", on=['month','year']) #col: ['month', 'year', 'tenhieuxe', 'sum', 'count_x', 'count_y'],
    data['tile']=data['count_x']/data['count_y']*100
    # data= data_xe_hieuxe_psc()
    for tenhieuxe, luotsua, thanhtien, ti_le, stt  in zip(data['tenhieuxe'], data['count_x'], data['sum_x'], data['tile'], data.index):
        CT_BaoCaoDoanhSO.objects.create(tenhieuxe=tenhieuxe,luotsua=luotsua,thanhtien=thanhtien,ti_le=ti_le,STT = stt)

    # ===============================================================
    for month, year, tongdoanhso in zip(total['month'],total['year'],total['sum']):
        BaoCaoDoanhSo.objects.create(month =month,year = year, tongdoanhso= tongdoanhso)

    if BaoCaoDoanhSo.objects.all().exists() ==False:
        return HttpResponse("update that bai")

    if CT_BaoCaoDoanhSO.objects.all().exists() ==False:
        return HttpResponse("update that bai")

    bcds = BaoCaoDoanhSo.objects.all()
    ct_bcds = CT_BaoCaoDoanhSO.objects.all()
    context={"bcds":bcds,"ct_bcds":ct_bcds}
    return render(request, 'gara/bao_cao_doanh_thu.html',context)

            

def search_bcds(request):
    if 'm'and'y' in request.GET:
        m = request.GET['m']
        y = request.GET['y']
        data = data_xe_hieuxe_psc()
        try:
            bcds = BaoCaoDoanhSo.objects.filter(month = m, year = y)
            search_ct_bcds = data.loc[(data['month']==int(m)) & (data['year']==int(y))]  
        except:
            try:
                if y=='':
                    bcds = BaoCaoDoanhSo.objects.filter(month = m)
                    search_ct_bcds = data.loc[(data['month']==int(m))]
                if m=='':
                    bcds = BaoCaoDoanhSo.objects.filter(year = y)
                    search_ct_bcds = data.loc[(data['year']==int(y))]
            except:
                bcds = BaoCaoDoanhSo.objects.all()
                search_ct_bcds = data
        
        b = search_ct_bcds.index
        ct_bcds = CT_BaoCaoDoanhSO.objects.filter(STT__in = list(b)) 
    else:
        bcds = BaoCaoDoanhSo.objects.all()
    
    context={"bcds":bcds, "ct_bcds":ct_bcds}
    return render(request, 'gara/bao_cao_doanh_thu.html',context)
   

# =========================================================

def get_bd(request):
    x = Xe.objects.all()
    hx = HieuXe.objects.all()
    kh = KhachHang.objects.all()
    df_x = pd.DataFrame(x.values())
    df_hx = pd.DataFrame(hx.values())
    df_kh = pd.DataFrame(kh.values())
    df_xhx = df_x.join(df_hx.set_index("mahieuxe"), on = "mahieuxe_id")
    data = df_xhx.join(df_kh.set_index("makhachhang"), on = "makhachhang_id")    
    df = data[["bienso","tenhieuxe","tenkhachhang","tienno"]]
    return render(request, 'gara/search_xe.html', {'df':df})

def data_tracuuxe():
    x = Xe.objects.all()
    hx = HieuXe.objects.all()
    kh = KhachHang.objects.all()
    df_x = pd.DataFrame(x.values())
    df_hx = pd.DataFrame(hx.values())
    df_kh = pd.DataFrame(kh.values())
    df_xhx = df_x.join(df_hx.set_index("mahieuxe"), on = "mahieuxe_id")
    data = df_xhx.join(df_kh.set_index("makhachhang"), on = "makhachhang_id")
    return data
    
def after_search(request):
    
    data = data_tracuuxe()
    # if "tukhoa" and "bienso" and "baocao" in request.GET:
    if  "bienso"  in request.GET:
        kh = request.GET['khachhang']
        bs = request.GET['bienso']
        hx = request.GET['hieuxe']
        print("=======: ",kh == '' , hx == '' )
        
        if kh == '' and hx == '':
            a = data.loc[(data["bienso"].str.contains(bs))]
        elif bs == '' and kh == '':
            a = data.loc[(data["tenhieuxe"].str.contains(hx))]
        elif bs == '' and hx == '':
            a = data.loc[(data["tenkhachhang"].str.contains(kh))]
        elif hx == '':
            a = data.loc[(data["bienso"].str.contains(bs)) & (data["tenkhachhang"].str.contains(kh)) ]
        elif bs == '':
            a = data.loc[(data["tenhieuxe"].str.contains(hx)) & (data["tenkhachhang"].str.contains(kh)) ]
        elif kh == '':
            a = data.loc[(data["tenhieuxe"].str.contains(hx)) & (data["bienso"].str.contains(bs)) ]
        else:
            a = data.loc[(data["tenhieuxe"].str.contains(hx)) & (data["bienso"].str.contains(bs)) & (data["tenkhachhang"].str.contains(kh)) ]
        df = a[["bienso","tenhieuxe","tenkhachhang","tienno"]]
    else:             
        df = data[["bienso","tenhieuxe","tenkhachhang","tienno"]]
    return render(request, 'gara/search_xe.html', {'df':df})
