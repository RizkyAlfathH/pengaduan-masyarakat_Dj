from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('masyarakat', 'Masyarakat'),
        ('petugas', 'Petugas'),
        ('admin', 'Administrator'),
    ]

    nik = models.CharField(max_length=16, unique=True, null=True, blank=True)
    nama = models.CharField(max_length=100, default='Anonim')  # Hanya satu field nama
    telp = models.CharField(max_length=13, null=True, blank=True)
    alamat = models.TextField(null=True, blank=True)
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='masyarakat')

    def __str__(self):
        return f"{self.username} ({self.role})"