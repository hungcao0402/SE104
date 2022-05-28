from django.urls import path
from . import views

app_name='gara'

urlpatterns = [
    path('nhap_biensothutien',views.nhapbienso_phieuthu,name='view-request'),
    path('dien_phieuthu/<int:maxe>',views.xacnhan_phieuthu,name='view-view'),
    path('view_phieuthu/<int:maphieuthutien>',views.view_phieuthu,name='view-view'),
    path('',views.nhapbiensosua,name='nhapbiensosua'),
    path('view_phieusua/<int:maphieusuachua>',views.view_phieusua,name='view-phieusua'),  #
    path('view_ctphieusua/<int:mact_phieusuachua>',views.view_ctphieusuachua,name='view_ctphieusuachua')
]