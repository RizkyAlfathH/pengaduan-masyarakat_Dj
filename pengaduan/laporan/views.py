from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Pengaduan, Tanggapan
from .forms import PengaduanForm, TanggapanForm, RegisterForm
from django.contrib.auth.models import User

STATUS_MAP = {
    "tunggu": 1,
    "proses": 2,
    "selesai": 3,
}

@login_required
def admin_dashboard(request):
    filter_status = request.GET.get('filter_status', '')
    pengaduan_list = Pengaduan.objects.select_related('user').order_by('-tgl_pengaduan')

    if filter_status in STATUS_MAP:
        pengaduan_list = pengaduan_list.filter(status=STATUS_MAP[filter_status])

    total_laporan = Pengaduan.objects.count()
    menunggu_verifikasi = Pengaduan.objects.filter(status=STATUS_MAP["tunggu"]).count()
    dalam_proses = Pengaduan.objects.filter(status=STATUS_MAP["proses"]).count()
    selesai = Pengaduan.objects.filter(status=STATUS_MAP["selesai"]).count()

    paginator = Paginator(pengaduan_list, 5)
    page_number = request.GET.get('page')
    pengaduan = paginator.get_page(page_number)

    context = {
        'pengaduan': pengaduan,
        'total_laporan': total_laporan,
        'menunggu_verifikasi': menunggu_verifikasi,
        'dalam_proses': dalam_proses,
        'selesai': selesai,
        'filter_status': filter_status,
    }
    return render(request, 'dashboard/admin.html', context)

@login_required
def admin_verifikasi_update(request, pk):
    pengaduan = get_object_or_404(Pengaduan, pk=pk)
    if request.method == 'POST':
        pengaduan.status = STATUS_MAP["proses"]
        pengaduan.save()
        messages.success(request, "Pengaduan berhasil diverifikasi.")
        return redirect('admin_dashboard')
    return render(request, 'laporan/verifikasi_update.html', {'pengaduan': pengaduan})

@login_required
def buat_pengaduan(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'masyarakat':
        messages.error(request, "Hanya masyarakat yang dapat membuat pengaduan.")
        return redirect('dashboard')

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
    paginator = Paginator(pengaduan_list, 5)
    page_number = request.GET.get('page')
    pengaduan = paginator.get_page(page_number)
    return render(request, 'laporan/daftar_pengaduan.html', {'pengaduan': pengaduan})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Username atau password salah.")
    return render(request, "users/login.html")

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registrasi berhasil! Silakan login.")
            return redirect("login")
        messages.error(request, "Ada kesalahan dalam registrasi.")
    else:
        form = RegisterForm()
    return render(request, "users/register.html", {"form": form})

@login_required
def petugas_dashboard(request):
    return render(request, 'laporan/petugas_dashboard.html')

@login_required
def masyarakat_dashboard(request):
    return render(request, 'dashboard/masyarakat.html')

def laporan_list(request):
    filter_status = request.GET.get('filter_status')
    laporan = Pengaduan.objects.all().order_by('-tgl_pengaduan')

    if filter_status in STATUS_MAP:
        laporan = laporan.filter(status=STATUS_MAP[filter_status])
    
    return render(request, 'laporan/laporan_list.html', {'laporan': laporan})

def dashboard(request):
    return render(request, 'dashboard/admin.html')

# laporan/views.py
from django.shortcuts import render, get_object_or_404
from .models import Pengaduan  # Sesuaikan dengan model laporan kamu

def admin_tanggapan_show(request, id):
    laporan = get_object_or_404(Pengaduan, id=id)
    return render(request, 'laporan/form_tanggapan.html', {'laporan': laporan})
