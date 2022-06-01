from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

#class ThamSo(models.Model):

class KhachHang(models.Model):
    makhachhang=models.AutoField(primary_key=True)
    tenkhachhang=models.CharField(max_length=40)
    diachi=models.CharField(max_length=100)
    dienthoai=models.PositiveIntegerField()
    def __str__(self):
        return self.tenkhachhang  
class HieuXe(models.Model):
    mahieuxe=models.AutoField(primary_key=True)
    tenhieuxe=models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.tenhieuxe
class Xe(models.Model): 
    maxe=models.AutoField(primary_key=True)
    bienso=models.CharField(max_length=20,unique=True)
    makhachhang=models.ForeignKey(KhachHang,on_delete=models.CASCADE)
    mahieuxe=models.ForeignKey(HieuXe,on_delete=models.CASCADE)
    tienno=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.bienso


class PhieuTiepNhan(models.Model):
    maphieutiepnhan = models.AutoField(primary_key=True)
    tenchuxe = models.CharField(max_length=40,null=False)
    bienso = models.PositiveIntegerField(null=False)
    diachi = models.CharField(max_length=100,null=False)
    hieuxe = models.ForeignKey(HieuXe, on_delete=models.DO_NOTHING)
    dienthoai =  models.PositiveIntegerField(null=False)
    date=models.DateField(auto_now=True)
    def __str__(self):
        return f"Tên chủ xe: {self.tenchuxe}, Biển số: {self.bienso}"

class PhieuThuTien(models.Model):
    maphieuthutien=models.AutoField(primary_key=True)
    maxe=models.ForeignKey(Xe,on_delete=models.CASCADE)
    ngaythu=models.DateField(auto_now_add=True)
    sotienthu=models.PositiveIntegerField()
class PhieuSuaChua(models.Model):
    maphieusuachua=models.AutoField(primary_key=True)
    maxe=models.ForeignKey(Xe,on_delete=models.CASCADE)
    tongthanhtien=models.PositiveIntegerField(default=0)
    ngaylapphieu=models.DateField(auto_now_add=True)   
    def __str__(self):
        return f"{self.maphieusuachua}"
class TienCong(models.Model):
    matiencong=models.AutoField(primary_key=True)
    loaitiencong=models.CharField(max_length=50, unique=True) 
    tiencong=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.loaitiencong
class CT_PhieuSuaChua(models.Model):
    mact_phieusuachua=models.AutoField(primary_key=True)
    maphieusuachua=models.ForeignKey(PhieuSuaChua,on_delete=models.CASCADE)
    solan=models.PositiveIntegerField()
    matiencong=models.ForeignKey(TienCong,on_delete=models.CASCADE)
    tiencong=models.PositiveIntegerField()
    tongtienvattu=models.PositiveIntegerField(default=0)
    noidung=models.CharField(max_length=100)
    tongtien=models.PositiveIntegerField(default=0)
class VatTuPhuTung(models.Model):
    mavattuphutung=models.AutoField(primary_key=True)
    tenvattuphutung=models.CharField(max_length=50)
    dongia=models.PositiveIntegerField()
    soluong=models.PositiveIntegerField()
    def __str__(self):
        return self.tenvattuphutung

class CT_VatTuPhuTung(models.Model):
    mact_vattuphutung=models.AutoField(primary_key=True)
    mavattuphutung=models.ForeignKey(VatTuPhuTung,on_delete=models.CASCADE)
    mact_phieusuachua=models.ForeignKey(CT_PhieuSuaChua,on_delete=models.CASCADE)
    soluong=models.PositiveIntegerField()
    dongia=models.PositiveIntegerField()
    tongthanhtien=models.PositiveIntegerField()
class PhieuNhapVTPT(models.Model):
    maphieunhapvtpt=models.AutoField(primary_key=True)
    mavattuphutung=models.ForeignKey(VatTuPhuTung,on_delete=models.CASCADE,null=True)
    soluong=models.PositiveIntegerField(default=0)
    dongia=models.PositiveIntegerField(default=0)
    date=models.DateField(auto_now_add=True,null=True)
# class BaoCaoDoanhSo(models.Model):
#     mabaocaodoanhso=models.AutoField(primary_key=True)
#     thoidiem=models.DateField(auto_now_add=True)
#     tongdoanhso=models.PositiveIntegerField(default=0)

# class CT_BaoCaoDoanhSO(models.Model):
#     mact_baocaodoanhso=models.AutoField(primary_key=True)
#     mabaocaodoanhso = models.ForeignKey(BaoCaoDoanhSo,on_delete=models.CASCADE)
#     maphieusuachua = models.ForeignKey(PhieuSuaChua,on_delete=models.CASCADE)
#     luotsua = models.PositiveIntegerField(default=0)
#     thanhtien = models.PositiveIntegerField(default=0)

from django.db.models.functions import ExtractMonth,ExtractYear
class BaoCaoDoanhSo(models.Model):
    mabaocaodoanhso=models.AutoField(primary_key=True)
    thoidiem=models.DateField(auto_now_add=True)
    month = models.PositiveIntegerField(default=0)
    year = models.PositiveIntegerField(default=0)
    tongdoanhso=models.PositiveIntegerField(default=0)

class CT_BaoCaoDoanhSO(models.Model):
    mact_baocaodoanhso=models.AutoField(primary_key=True)
    # mabaocaodoanhso = models.ForeignKey(BaoCaoDoanhSo,on_delete=models.CASCADE)
    # mahieuxe = models.ForeignKey(HieuXe, on_delete=models.CASCADE)
    STT = models.PositiveIntegerField(default=0)
    tenhieuxe = models.CharField(max_length=200,default="")
    luotsua = models.PositiveIntegerField(default=0)
    thanhtien = models.PositiveIntegerField(default=0)
    ti_le = models.FloatField(default=0)
    
class BaoCaoTon(models.Model):
    MaBCT=models.AutoField(primary_key=True)
    date = models.DateField(auto_now=True)

class ct_baocaoton(models.Model):
    MaBCT = models.ForeignKey(BaoCaoTon, on_delete=models.CASCADE)
    MaVTPT = models.ForeignKey(VatTuPhuTung, on_delete=models.CASCADE)
    TonDau =  models.PositiveIntegerField(null=False)
    PhatSinh =  models.PositiveIntegerField(null=False)
    TonCuoi = models.PositiveIntegerField(null=False)

# class ThamSo(models.Model):
#     mathamso=models.AutoField(primary_key=True)
#     tenthamso=models.CharField(max_length=20)
#     giatri=models.PositiveIntegerField()

# ThamSo
class QuyDinhHienHanh(models.Model):
    # MaThamSo = models.ForeignKey(ThamSo, on_delete= models.CASCADE)
    MaThamSo = models.AutoField(primary_key=True)
    TenThamSo = models.TextField(default='')
    GiaTri = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.TenThamSo

# class TaiKhoan(models.Model):
#     TenTaiKhoan = models.CharField(max_length=1)
#     MatKhau = models.CharField(max_length=25)
class Staff(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    username = models.CharField(max_length=15, default='AnonymousUser', unique=True)
    firstname = models.CharField(max_length=15, default='Anonymous')
    lastname = models.CharField(max_length=10, default='User')
    password = models.CharField(max_length=20,default='')
    profile_pic= models.ImageField(upload_to='static/profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    emails = models.EmailField(max_length=90, default='anonymous@gmail.com', null=True)
    is_admin = models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.firstname+" "+self.lastname
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.username
