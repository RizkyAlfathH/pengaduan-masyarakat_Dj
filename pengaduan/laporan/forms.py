from django import forms
from django.contrib.auth.models import User  # Import model User bawaan Django
from .models import Pengaduan, Tanggapan

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['kategori', 'lokasi', 'isi_laporan', 'foto']

def clean(self):
    cleaned_data = super().clean()
    if self.instance.pk:  # Cek apakah instance sudah ada di database
        user = self.instance.user
        if user and user.role != 'masyarakat':
            raise forms.ValidationError("Hanya pengguna dengan role 'masyarakat' yang bisa membuat pengaduan.")
    return cleaned_data

class TanggapanForm(forms.ModelForm):
    class Meta:
        model = Tanggapan
        fields = ['tanggapan']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']