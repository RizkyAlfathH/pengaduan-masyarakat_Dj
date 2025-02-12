from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Pengaduan, Tanggapan
from .forms import PengaduanForm, TanggapanForm, RegisterForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator

@login_required
def dashboard(request):
    if request.user.role == 'admin':
        return redirect('admin_dashboard')
    elif request.user.role == 'petugas':
        return redirect('petugas_dashboard')
    else:
        return redirect('masyarakat_dashboard')

@login_required
def buat_pengaduan(request):
    if request.method == 'POST':
        form = PengaduanForm(request.POST, request.FILES)
        if form.is_valid():
            pengaduan = form.save(commit=False)
            pengaduan.user = request.user
            pengaduan.save()
            messages.success(request, "Pengaduan berhasil diajukan.")
            return redirect('dashboard')
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
            # Redirect berdasarkan role
            if user.role == 'admin':
                return redirect('admin_dashboard')
            elif user.role == 'petugas':
                return redirect('petugas_dashboard')
            elif user.role == 'masyarakat':
                return redirect('masyarakat_dashboard')
            else:
                return redirect('dashboard')
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
            messages.error(request, "Ada kesalahan dalam registrasi.")
    else:
        form = RegisterForm()
    
    return render(request, "users/register.html", {"form": form})

@login_required
def admin_dashboard(request):
    # Filter berdasarkan status
    filter_status = request.GET.get('filter_status', '')
    if filter_status:
        pengaduan_list = Pengaduan.objects.filter(status=filter_status).order_by('-tgl_pengaduan')
    else:
        pengaduan_list = Pengaduan.objects.all().order_by('-tgl_pengaduan')

    # Pagination
    paginator = Paginator(pengaduan_list, 5)  # 5 laporan per halaman
    page_number = request.GET.get('page')
    pengaduan = paginator.get_page(page_number)

    # Statistik laporan
    total_laporan = Pengaduan.objects.count()
    menunggu_verifikasi = Pengaduan.objects.filter(status='tunggu').count()
    dalam_proses = Pengaduan.objects.filter(status='proses').count()
    selesai = Pengaduan.objects.filter(status='selesai').count()

    context = {
        'pengaduan': pengaduan,
        'total_laporan': total_laporan,
        'menunggu_verifikasi': menunggu_verifikasi,
        'dalam_proses': dalam_proses,
        'selesai': selesai,
        'filter_status': filter_status,
    }
    return render(request, 'laporan/admin_dashboard.html', context)

@login_required
def petugas_dashboard(request):
    return render(request, 'laporan/petugas_dashboard.html')

@login_required
def masyarakat_dashboard(request):
    return render(request, 'dashboard/masyarakat.html')

@login_required
def form_pengaduan(request):
    return render(request, 'laporan/form_pengaduan.html')

def laporan_list(request):
    status_map = {
    "tunggu": 0,
    "proses": 1,
    "selesai": 2,
}
    filter_status = request.GET.get('filter_status')  # Pastikan ada di dalam fungsi
    laporan = Pengaduan.objects.all()

    if filter_status:
        laporan = laporan.filter(status=filter_status)

    return render(request, 'laporan_list.html', {'laporan': laporan})