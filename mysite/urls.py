from django.contrib import admin
from django.urls import path, include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import *
from mysite.authentication import login, logout, registrasi

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', index),
    path('artikel/<int:id>', detail, name="detail"),
    path('kategori/<str:nama_kategori>/', kategori_filter, name="kategori_filter"),
    path('artikel-not-found', not_found, name="not_found"),
    path('kontak', kontak, name='kontak'),
    path('galeri', galeri, name='galeri'),
    
    path('dashboard', dashboard, name='dashboard'),
    path('dashboard/artikel-list', artikel_list, name='artikel_list'),

    path('dashboard/', include("artikel.urls")),

########################## Authentication ##############################
    path('auth-login', login, name='login'),
    path('auth-logout', logout, name='logout'),
    path('auth-registrasi', registrasi, name='registrasi'),
]

########################## Untuk Media ##############################
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)