from django import forms
from django.contrib.auth.models import User  # Import model User bawaan Django
from .models import Pengaduan, Tanggapan

class PengaduanForm(forms.ModelForm):
    class Meta:
        model = Pengaduan
        fields = ['isi_laporan', 'foto', 'lokasi']

class TanggapanForm(forms.ModelForm):
    class Meta:
        model = Tanggapan
        fields = ['tanggapan']

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
