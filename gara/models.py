from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

#class ThamSo(models.Model):

class vattuphutung(models.Model):
    mavattuphutrung = models.AutoField(primary_key=True)
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

    def save(self, *args, **kwargs):
            
            if PhieuTiepNhan.objects.filter(date).exists():
                print('Video with field_boolean=True exists')
            else:
                super(Video, self).save(*args, **kwargs)


    def __str__(self):
        return f"Tên chủ xe: {self.tenchuxe}, Biển số: {self.bienso}"


class baocaoton(models.Model):
    MaPhuTung = models.ForeignKey(vattuphutung, on_delete=models.DO_NOTHING)
    TonDau =  models.PositiveIntegerField(null=False)
    PhatSinh =  models.PositiveIntegerField(null=False)
    TonCuoi=  models.PositiveIntegerField(null=False)
    thang = models.DateField()

# class TaiKhoan(models.Model):
#     TenTaiKhoan = models.CharField(max_length=1)
#     MatKhau = models.CharField(max_length=25)
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    username = models.CharField(max_length=15, default='AnonymousUser', unique=True)
    firstname = models.CharField(max_length=15, default='Anonymous')
    lastname = models.CharField(max_length=10, default='User')
    password = models.CharField(max_length=20,default='')
    profile_pic= models.ImageField(upload_to='static/profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    emails = models.EmailField(max_length=90, default='anonymous@gmail.com', null=True)
    @property
    def get_name(self):
        return self.firstname+" "+self.lastname
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.username
