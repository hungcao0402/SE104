from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

#class ThamSo(models.Model):

# class phieusuachua(models.Model):

class nhapvattuphutung(models.Model):
    mavattuphutrung = models.ForeignKey(vattuphutung)
    soluong = models.PositiveIntegerField(null=False)
    thoidiem = models.DateField(auto_now=True)

class vattuphutung(models.Model):
    mavattuphutung = models.AutoField(primary_key=True)
    ten = models.CharField(max_length=40,null=False) 
    soluong = models.PositiveIntegerField(null=False)
    dongia = models.PositiveIntegerField(null=False)
    # loai=

class KhachHang(models.Model):
    makhachhang = models.AutoField(primary_key=True)
    tenchuxe = models.CharField(max_length=40,null=False) 
    diachi = models.CharField(max_length=100,null=False)
    dienthoai =  models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return self.name

class HieuXe(models.Model):
    name = models.CharField(max_length=40,null=False)    
    def __str__(self):
        return self.name

class PhieuTiepNhan(models.Model):
    maphieutiepnhan = models.AutoField(primary_key=True)
    tenchuxe = models.CharField(max_length=40,null=False)
    bienso = models.PositiveIntegerField(null=False)
    diachi = models.CharField(max_length=100,null=False)
    hieuxe = models.ForeignKey(HieuXe, on_delete=models.DO_NOTHING)
    dienthoai =  models.PositiveIntegerField(null=False)
    date=models.DateField(auto_now=True)

    # def save(self, *args, **kwargs):
            
    #         if PhieuTiepNhan.objects.filter(date).exists():
    #             print('Video with field_boolean=True exists')
    #         else:
    #             super(Video, self).save(*args, **kwargs)


    def __str__(self):
        return f"Tên chủ xe: {self.tenchuxe}, Biển số: {self.bienso}"


class baocaoton(models.Model):
    thoidiem = models.DateField(auto_now=True)

class ct_baocaoton(models.Model):
    MaBCT = models.ForeignKey(baocaoton, on_delete=models.CASCADE)
    MaVTPT = models.ForeignKey(vattuphutung, on_delete=models.CASCADE)
    TonDau =  models.PositiveIntegerField(null=False)
    PhatSinh =  models.PositiveIntegerField(null=False)
    TonCuoi = models.PositiveIntegerField(null=False)
    MaPhuTung = models.ForeignKey(vattuphutung, on_delete=models.DO_NOTHING)
