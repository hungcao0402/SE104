from django.urls import path
from . import views

app_name='gara'

urlpatterns = [
    path('add-request', views.tiep_nhan,name='add-request'),
    path('request',views.view_request,name='view-request'),
    path('view_baocaoton', views.view_baocaoton),
    path('baocaoton', views.baocaoton_luachon),
    path('save_baocaoton',views.save_baocaoton)
]