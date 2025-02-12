from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import logout


def home_view(request):
    context = {
        'user': request.user if request.user.is_authenticated else None,
    }
    return render(request, 'home.html', context)  # Pastikan template home.html ada di folder yang sesuai

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")  # Ubah ke 'home'
        else:
            messages.error(request, "Username atau password salah.")
    
    return render(request, "users/login.html")

def register_view(request):
    if request.method == "POST":
        nik = request.POST.get("nik")
        nama = request.POST.get("nama")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        telp = request.POST.get("telp")
        alamat = request.POST.get("alamat")

        if password1 == password2:  # Validasi dasar
            if CustomUser.objects.filter(username=username).exists():
                messages.error(request, "Username sudah terdaftar. Gunakan username lain.")
            else:
                CustomUser.objects.create_user(
                    username=username, password=password1, nik=nik, nama=nama, telp=telp, alamat=alamat
                )
                messages.success(request, "Registrasi berhasil! Silakan login.")
                return redirect("login")
        else:
            messages.error(request, "Password dan konfirmasi password tidak cocok.")
    
    return render(request, "users/register.html")

def logout_view(request):
    logout(request)
    return redirect("home")

def laporan_view(request):
    return render(request, "laporan.html")  # Pastikan kamu punya laporan.html di folder templates


