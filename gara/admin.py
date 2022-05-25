from django.contrib import admin
from .models import *
# Register your models here.
# class KhachHangAdmin(admin.ModelAdmin):
#     list_display= ('makhachhang','tenkhachhang','diachi','dienthoai','email')
# class PhieuThuAdmin(admin.ModelAdmin):
#     list_display= ('maphieuthutien','maxe','ngaythu','sotienthu')
# class XeAdmin(admin.ModelAdmin):
#     list_display=('maxe','bienso','makhachhang','mahieuxe','ngaytiepnhan','tienno')
# class HieuXeAdmin(admin.ModelAdmin):
#     list_display=('mahieuxe','tenhieuxe')
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
admin.site.register(CT_PhieuNhapVTPT)
admin.site.register(BaoCaoDoanhSo)
admin.site.register(CT_BaoCaoDoanhSO)
admin.site.register(ThamSo)
admin.site.register(BaoCaoTon)
