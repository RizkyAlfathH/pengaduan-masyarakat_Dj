from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Pengaduan, Tanggapan
from .forms import PengaduanForm, TanggapanForm, RegisterForm
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return render(request, 'dashboard/admin.html')
    elif request.user.role == 'petugas':
        return render(request, 'dashboard/petugas.html')
    else:
        return render(request, 'dashboard/masyarakat.html')

@login_required
def buat_pengaduan(request):
    if request.method == 'POST':
        form = PengaduanForm(request.POST, request.FILES)
        if form.is_valid():
            pengaduan = form.save(commit=False)
            pengaduan.user = request.user
            pengaduan.save()

            # Redirect berdasarkan role user
            if request.user.role == 'admin':
                return redirect('admin_dashboard')
            elif request.user.role == 'petugas':
                return redirect('petugas_dashboard')
            else:
                return redirect('masyarakat_dashboard')
    else:
        form = PengaduanForm()
    
    return render(request, 'laporan/form_pengaduan.html', {'form': form})

@login_required
def daftar_pengaduan(request):
    pengaduan_list = Pengaduan.objects.all().order_by('-tgl_pengaduan')
    return render(request, 'laporan/daftar_pengaduan.html', {'pengaduan_list': pengaduan_list})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Username atau password salah.")
    return render(request, "users/login.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrasi berhasil! Silakan login.")
            return redirect("login")
        else:
            print(form.errors)
            messages.error(request, "Ada kesalahan dalam registrasi.")
    else:
        form = RegisterForm()
    
    return render(request, "users/register.html", {"form": form})

@login_required
def admin_dashboard(request):
    return render(request, 'laporan/admin_dashboard.html')

@login_required
def petugas_dashboard(request):
    return render(request, 'laporan/petugas_dashboard.html')

@login_required
def masyarakat_dashboard(request):
    return render(request, 'dashboard/masyarakat.html')

@login_required
def form_pengaduan(request):
    return render(request, 'laporan/form_pengaduan.html')
