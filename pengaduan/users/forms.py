from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2', 'nik', 'telp', 'alamat', 'role']
        widgets = {
            'nik': forms.TextInput(attrs={'placeholder': 'Masukkan NIK'}),
            'telp': forms.TextInput(attrs={'placeholder': 'Masukkan Nomor Telepon'}),
            'alamat': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Masukkan Alamat'}),
        }

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['nik', 'nama', 'username', 'password1', 'password2', 'telp', 'alamat']
        widgets = {
            'nik': forms.TextInput(attrs={'placeholder': 'Masukkan NIK 16 digit'}),
            'nama': forms.TextInput(attrs={'placeholder': 'Masukkan Nama Lengkap'}),
            'telp': forms.TextInput(attrs={'placeholder': 'Masukkan Nomor Telepon'}),
            'alamat': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Masukkan Alamat'}),
        }

# users/forms.py
from django import forms
from .models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }