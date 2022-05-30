from django.urls import path, include
from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name='gara'

urlpatterns = [
    path('', views.home, name='home'),
    path('admin', admin.site.urls),
    path('add-request', views.tiep_nhan,name='add-request'),
    path('view-request',views.view_request,name='view-request'),
    url(r'^login/$', views.customer_login_view, name='login'),
    url( r'^logout/$',auth_views.LogoutView.as_view(template_name="profile/logout.html"), name="logout"),
    path('create_new_staff', views.createStaffAccount , name = 'create-staff-account'),
    path('',include('django.contrib.auth.urls')),
    path('profile/<username>', views.profile, name = 'profile'),
    path('dashboard/<username>', views.customer_dashboard_view, name = 'dashboard'),
    path('edit-profile/<username>', views.edit_customer_profile_view, name='edit-profile'),
    path('edit-account/<username>', views.edit_customer_account_view, name='edit-account'),
    path('<username>/nhap_biensothutien',views.nhapbienso_phieuthu,name='view-request'),
    path('<username>/nhap_phieuthu/<int:maxe>',views.xacnhan_phieuthu,name='view-view'),
    path('<username>/view_phieuthu/<int:maphieuthutien>',views.view_phieuthu,name='view-view'),
    path('<username>/nhap_biensosua',views.nhapbiensosua,name='nhapbiensosua'),
    path('<username>/view_phieusua/<int:maphieusuachua>',views.view_phieusua,name='view-phieusua'),
    path('<username>/view_ctphieusua/<int:mact_phieusuachua>',views.view_ctphieusuachua,name='view_ctphieusuachua'),
    path('<username>/delete_ctphieusua/<int:mact_phieusuachua>',views.delete_ctphieusua,name='delete_ctphieusua'),
    path('<username>/delete_chitietvattu/<int:mact_vattuphutung>/<int:mact_phieusuachua>/<int:maphieusuachua>',views.delete_chitietvattu,name='delete_chitietvattu')
]