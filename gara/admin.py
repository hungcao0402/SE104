from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
# Register your models here.
admin.site.register(Staff)
admin.site.register(KhachHang)
admin.site.register(PhieuThuTien)
admin.site.register(Xe)
admin.site.register(HieuXe)
admin.site.register(PhieuSuaChua)
admin.site.register(TienCong)
admin.site.register(CT_PhieuSuaChua)
admin.site.register(VatTuPhuTung)
admin.site.register(CT_VatTuPhuTung)
admin.site.register(PhieuNhapVTPT)
admin.site.register(BaoCaoDoanhSo)
admin.site.register(CT_BaoCaoDoanhSO)
admin.site.register(QuyDinhHienHanh)
admin.site.register(BaoCaoTon)
admin.site.register(PhieuTiepNhan)
