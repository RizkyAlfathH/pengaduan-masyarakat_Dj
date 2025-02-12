from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('tanggapan/<int:id>/', views.admin_tanggapan_show, name='admin_tanggapan_show'),
    path('verifikasi/update/<int:id>/', views.admin_verifikasi_update, name='admin_verifikasi_update'),
    path('petugas/', views.petugas_dashboard, name='petugas_dashboard'),
    path('masyarakat/', views.masyarakat_dashboard, name='masyarakat_dashboard'),
    path('laporan/', views.daftar_pengaduan, name='daftar_pengaduan'),
    path('buat-pengaduan/', views.buat_pengaduan, name='buat_pengaduan'),
    
    # Login dan Register
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    
    # Dashboard umum yang redirect sesuai role
    path('dashboard/', views.dashboard, name='dashboard'),
]

# Handling untuk static files dalam mode pengembangan
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
