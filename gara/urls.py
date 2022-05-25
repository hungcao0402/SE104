from django.urls import path
from . import views

app_name='gara'

urlpatterns = [
    path('',views.tao_form,name='view-request'),
    path('dien_phieuthu/<int:maxe>',views.xacnhan_phieuthu,name='view-view'),
    path('view_phieuthu/<int:maphieuthutien>',views.view_phieuthu,name='view-view')
]