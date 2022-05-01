from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


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


#class ThamSo(models.Model):


# class Request(models.Model):
#     cat=(('two wheeler with gear','two wheeler with gear'),('two wheeler without gear','two wheeler without gear'),('three wheeler','three wheeler'),('four wheeler','four wheeler'))
#     category=models.CharField(max_length=50,choices=cat)

#     vehicle_no=models.PositiveIntegerField(null=False)
#     vehicle_name = models.CharField(max_length=40,null=False)
#     vehicle_model = models.CharField(max_length=40,null=False)
#     vehicle_brand = models.CharField(max_length=40,null=False)

#     problem_description = models.CharField(max_length=500,null=False)
#     date=models.DateField(auto_now=True)
#     cost=models.PositiveIntegerField(null=True)

#     customer=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
#     #mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)

#     stat=(('Pending','Pending'),('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'),('Released','Released'))
#     status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)

#     def __str__(self):
#         return self.problem_description
