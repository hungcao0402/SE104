from calendar import month
from statistics import mode
# from typing_extensions import Self
from django.db import models
from django.utils import timezone
from django.db.models import Sum, Count
from django.contrib.auth.models import User

class KhachHang(models.Model):
    makhachhang=models.AutoField(primary_key=True)
    tenkhachhang=models.CharField(max_length=40)
    diachi=models.CharField(max_length=100)
    dienthoai=models.IntegerField()
    email=models.CharField(max_length=40)
    def __str__(self):
        return self.tenkhachhang  

class HieuXe(models.Model):
    mahieuxe=models.AutoField(primary_key=True)
    tenhieuxe=models.CharField(max_length=30)
    def __str__(self):
        return self.tenhieuxe

class Xe(models.Model): 
    maxe=models.AutoField(primary_key=True)
    bienso=models.CharField(max_length=20)
    makhachhang=models.ForeignKey(KhachHang,on_delete=models.CASCADE)
    mahieuxe=models.ForeignKey(HieuXe,on_delete=models.CASCADE, related_name= "hieuxe")
    ngaytiepnhan=models.DateField(auto_now_add=True)
    tienno=models.IntegerField(default=0)
    def __int__(self):
        return self.bienso

class PhieuThuTien(models.Model):
    maphieuthutien=models.AutoField(primary_key=True)
    maxe=models.ForeignKey(Xe,on_delete=models.CASCADE, related_name="xe_thutien")
    ngaythu=models.DateField()
    sotienthu=models.IntegerField()

class PhieuSuaChua(models.Model):
    maphieusuachua=models.AutoField(primary_key=True)
    maxe=models.ForeignKey(Xe,on_delete=models.CASCADE, related_name="xe_suachua")
    tongthanhtien=models.IntegerField(default=0)
    ngaylapphieu=models.DateField()

class TienCong(models.Model):
    matiencong=models.AutoField(primary_key=True)
    loaitiencong=models.CharField #check lai
    tiencong=models.IntegerField(default=0)

class CT_PhieuSuaChua(models.Model):
    mact_phieusuachua=models.AutoField(primary_key=True)
    maphieusuachua=models.ForeignKey(PhieuSuaChua,on_delete=models.CASCADE)
    solan=models.IntegerField()
    matiencong=models.ForeignKey(TienCong,on_delete=models.CASCADE)
    tiencong=models.IntegerField()
    noidung=models.CharField(max_length=100)
    tongtien=models.IntegerField(default=0)

class VatTuPhuTung(models.Model):
    mavattuphutung=models.AutoField(primary_key=True)
    tenvattuphutung=models.CharField(max_length=50)
    loaivattuphutung=models.CharField(max_length=50)
    dongia=models.IntegerField()
    soluong=models.IntegerField()

class CT_VatTuPhuTung(models.Model):
    mact_vattuphutung=models.AutoField(primary_key=True)
    mavattuphutung=models.ForeignKey(VatTuPhuTung,on_delete=models.CASCADE)
    mact_phieusuachua=models.ForeignKey(CT_PhieuSuaChua,on_delete=models.CASCADE)
    soluong=models.IntegerField()
    dongia=models.IntegerField()
    tongthanhtien=models.IntegerField()

class PhieuNhapVTPT(models.Model):
    maphieunhapvtpt=models.AutoField(primary_key=True)
    tongtien=models.IntegerField()
    thoidiem=models.DateField(auto_now_add=True)

class CT_PhieuNhapVTPT(models.Model):
    mact_phieunhapvtpt=models.AutoField(primary_key=True)
    mavattuphutung=models.ForeignKey(VatTuPhuTung,on_delete=models.CASCADE)
    maphieunhapvtpt=models.ForeignKey(PhieuNhapVTPT,on_delete=models.CASCADE)
    soluong=models.IntegerField()
    dongia=models.IntegerField()


from django.db.models.functions import ExtractMonth,ExtractYear
class BaoCaoDoanhSo(models.Model):
    mabaocaodoanhso=models.AutoField(primary_key=True)
    thoidiem=models.DateField(auto_now_add=True)
    month = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    tongdoanhso=models.IntegerField(default=0)


       

class CT_BaoCaoDoanhSO(models.Model):
    mact_baocaodoanhso=models.AutoField(primary_key=True)
    # mabaocaodoanhso = models.ForeignKey(BaoCaoDoanhSo,on_delete=models.CASCADE)
    # mahieuxe = models.ForeignKey(HieuXe, on_delete=models.CASCADE)
    STT = models.IntegerField(default=0)
    tenhieuxe = models.CharField(max_length=200,default="")
    luotsua = models.IntegerField(default=0)
    thanhtien = models.IntegerField(default=0)
    ti_le = models.FloatField(default=0)
    

# class Baocaodoanhso(models.Model):
#     mact_baocaodoanhso=models.AutoField(primary_key=True)
#     thoidiem=models.DateField(auto_now_add=True)
#     month = models.IntegerField(default=0)
#     year = models.IntegerField(default=0)
#     tongdoanhso=models.IntegerField(default=0) #ti le
#     tenhieuxe = models.CharField(max_length=200,default="")
#     luotsua = models.IntegerField(default=0)
#     thanhtien = models.IntegerField(default=0)
#     ti_le = models.FloatField(default=0)
    

class ThamSo(models.Model):
    mathamso=models.AutoField(primary_key=True)
    tenthamso=models.CharField(max_length=20)
    giatri=models.IntegerField()

class BaoCaoTon(models.Model):
    mabaocaoton=models.AutoField(primary_key=True)
    mavattuphutung=models.ForeignKey(VatTuPhuTung,on_delete=models.CASCADE)
    tondau=models.IntegerField()
    toncuoi=models.IntegerField()
    phatsinh=models.IntegerField()


# ThamSo
class QuyDinhHienHanh(models.Model):
    # MaThamSo = models.ForeignKey(ThamSo, on_delete= models.CASCADE)
    MaThamSo = models.AutoField(primary_key=True)
    TenThamSo = models.TextField(default='')
    GiaTri = models.IntegerField(default=0)

    def __str__(self):
        return self.TenThamSo