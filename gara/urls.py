from django.urls import path
from . import views

app_name='gara'

urlpatterns = [
    path('phieunhapvtpt',views.phieunhapvtpt,name='phieunhapvtpt'),
    path('view_ctphieunhapvtpt',views.view_ctphieunhapvtpt,name='view_ctphieunhapvtpt'),
    path('view_cappnhatvtpt/<int:mavattuphutung>',views.view_cappnhatvtpt,name='view-view')
]