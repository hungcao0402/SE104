from django.urls import path
from . import views

app_name='gara'

urlpatterns = [
    # path('',views.nhapbienso_phieuthu,name='view-request'),
    # path('dien_phieuthu/<int:maxe>',views.xacnhan_phieuthu,name='view-view'),
    # path('view_phieuthu/<int:maphieuthutien>',views.view_phieuthu,name='view-view'),

    # ==========================================
    #NGUYEN TRI
    # path('1', views.add_DoanhThu),
    # path('1', views.add_ct_DoanhThu),
    path('', views.Bao_Cao_Doanh_So),
    path('post_bsds',views.search_bcds, name="post_bsds"),
    path('thamso', views.regular_update, name="index"),
    path('save/',views.save_regular_update, name="save"),
    path('update_quydinh/<str:mts>/', views.update_quydinh, name = "update_quydinh"),
    path('delete_quydinh/<str:mts>/', views.delete_quydinh, name = "delete_quydinh"),

]