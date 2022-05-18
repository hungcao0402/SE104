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
    url(r'^login-customer/$', views.customer_login_view, name='login'),
    url( r'^logout-customer/$',auth_views.LogoutView.as_view(template_name="gara/logout.html"), name="logout"),
    path('signUp', views.sign_up, name = 'sign-up'),
    path('',include('django.contrib.auth.urls')),
    path('customer-profile/<username>', views.profile, name = 'customer-profile'),
    path('customer-dashboard/<username>', views.customer_dashboard_view, name = 'customer-dashboard'),
    path('customer-edit-profile/<username>', views.edit_customer_profile_view, name='customer-edit-profile'),
    path('customer-edit-account/<username>', views.edit_customer_account_view, name='customer-edit-account')
]