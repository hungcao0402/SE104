from django.urls import path
from . import views

app_name='gara'

urlpatterns = [
    path('', views.tiep_nhan,name='add_request'),
]