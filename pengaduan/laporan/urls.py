from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('petugas/', views.petugas_dashboard, name='petugas_dashboard'),
    path('masyarakat/', views.masyarakat_dashboard, name='masyarakat_dashboard'),
    path('laporan/', views.daftar_pengaduan, name='daftar_pengaduan'),
    path('buat-pengaduan/', views.buat_pengaduan, name='buat_pengaduan'),
]

# Tambahkan static URL handling jika dalam mode pengembangan
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
