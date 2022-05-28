from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User
from numpy import True_

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
    bienso=models.CharField(max_length=20,unique=True)
    makhachhang=models.ForeignKey(KhachHang,on_delete=models.CASCADE)
    mahieuxe=models.ForeignKey(HieuXe,on_delete=models.CASCADE)
    ngaytiepnhan=models.DateField(auto_now_add=True)
    tienno=models.IntegerField(default=0)
    def __str__(self):
        return self.bienso
class PhieuThuTien(models.Model):
    maphieuthutien=models.AutoField(primary_key=True)
    maxe=models.ForeignKey(Xe,on_delete=models.CASCADE)
    ngaythu=models.DateField(auto_now_add=True)
    sotienthu=models.IntegerField()
class PhieuSuaChua(models.Model):
    maphieusuachua=models.AutoField(primary_key=True)
    maxe=models.ForeignKey(Xe,on_delete=models.CASCADE)
    tongthanhtien=models.IntegerField(default=0)
    ngaylapphieu=models.DateField(auto_now_add=True)   
    def __str__(self):
        return f"{self.maphieusuachua}"
class TienCong(models.Model):
    matiencong=models.AutoField(primary_key=True)
    loaitiencong=models.CharField(max_length=50, unique=True) 
    tiencong=models.IntegerField(default=0)
    def __str__(self):
        return self.loaitiencong
class CT_PhieuSuaChua(models.Model):
    mact_phieusuachua=models.AutoField(primary_key=True)
    maphieusuachua=models.ForeignKey(PhieuSuaChua,on_delete=models.CASCADE)
    solan=models.IntegerField()
    matiencong=models.ForeignKey(TienCong,on_delete=models.CASCADE)
    tiencong=models.IntegerField()
    tongtienvattu=models.IntegerField(default=0)
    noidung=models.CharField(max_length=100)
    tongtien=models.IntegerField(default=0)
class VatTuPhuTung(models.Model):
    mavattuphutung=models.AutoField(primary_key=True)
    tenvattuphutung=models.CharField(max_length=50)
    loaivattuphutung=models.CharField(max_length=50)
    dongia=models.IntegerField()
    soluong=models.IntegerField()
    def __str__(self):
        return self.tenvattuphutung

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

class BaoCaoDoanhSo(models.Model):
    mabaocaodoanhso=models.AutoField(primary_key=True)
    thoidiem=models.DateField(auto_now_add=True)
    tongdoanhso=models.IntegerField(default=0)

class CT_BaoCaoDoanhSO(models.Model):
    mact_baocaodoanhso=models.AutoField(primary_key=True)
    mabaocaodoanhso = models.ForeignKey(BaoCaoDoanhSo,on_delete=models.CASCADE)
    maphieusuachua = models.ForeignKey(PhieuSuaChua,on_delete=models.CASCADE, )
    luotsua = models.IntegerField(default=0)
    thanhtien = models.IntegerField(default=0)

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


