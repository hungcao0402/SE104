from django.urls import path
from . import views

app_name='gara'

urlpatterns = [
    path('add-request', views.tiep_nhan,name='add-request'),
    path('view-request',views.view_request,name='view-request'),
    path('tham-so',views.CapNhatThamSo,name='tham-so'),

]