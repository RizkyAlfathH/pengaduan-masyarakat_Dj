"""
URL configuration for pengaduan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# urls.py
from django.contrib import admin
from django.urls import path, include
from users.views import home_view  # Import home_view yang benar

urlpatterns = [
    path('', home_view, name='home'),  # Menggunakan home_view untuk tampilan awal
    path('admin/', admin.site.urls),
    path('laporan/', include('laporan.urls')),  # Menghubungkan urls.py di laporan
    path('users/', include('users.urls')),      # Menghubungkan urls.py di users
]


