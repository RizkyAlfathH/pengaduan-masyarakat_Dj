from django.contrib import admin
from .models import Kategori, Pengaduan, Laporan, Tanggapan

admin.site.register(Kategori)
admin.site.register(Pengaduan)
admin.site.register(Laporan)
admin.site.register(Tanggapan)