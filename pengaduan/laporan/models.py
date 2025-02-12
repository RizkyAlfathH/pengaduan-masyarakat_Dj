from django.db import models
from users.models import CustomUser

class Pengaduan(models.Model):
    STATUS_CHOICES = [
        (1, 'Tunggu'),
        (2, 'Proses'),
        (3, 'Selesai'),
    ]

    KATEGORI_CHOICES = [
        ('Kebersihan', 'Kebersihan'),
        ('Keamanan', 'Keamanan'),
        ('Pelanggaran', 'Pelanggaran'),
        ('Fasilitas Umum', 'Fasilitas Umum'),
        ('Tidak Ditentukan', 'Tidak Ditentukan'),  # Tambahkan opsi default
    ]

    user = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'masyarakat'}
    )
    tgl_pengaduan = models.DateTimeField(auto_now_add=True)
    kategori = models.CharField(
        max_length=50, 
        choices=KATEGORI_CHOICES, 
        default='Tidak Ditentukan'
    )
    lokasi = models.CharField(max_length=255)
    isi_laporan = models.TextField()
    foto = models.ImageField(upload_to='bukti/', blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.user.username} - {self.kategori} ({self.get_status_display()})"

    def get_status_display(self):
        """Method untuk mendapatkan status dalam bentuk string ('Tunggu', 'Proses', 'Selesai')"""
        return dict(self.STATUS_CHOICES).get(self.status, "Unknown")


class Tanggapan(models.Model):
    pengaduan = models.ForeignKey(Pengaduan, on_delete=models.CASCADE)
    petugas = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'petugas'}
    )
    tgl_tanggapan = models.DateTimeField(auto_now_add=True)
    tanggapan = models.TextField()

    def __str__(self):
        return f"Tanggapan {self.id} untuk Pengaduan {self.pengaduan.id}"


class Laporan(models.Model):
    pengaduan = models.ForeignKey(Pengaduan, on_delete=models.CASCADE)
    admin = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={'role': 'admin'}
    )
    tgl_generate = models.DateTimeField(auto_now_add=True)
    deskripsi = models.TextField()

    def __str__(self):
        return f"Laporan {self.id} oleh {self.admin.username}"


class Kategori(models.Model):
    nama = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nama