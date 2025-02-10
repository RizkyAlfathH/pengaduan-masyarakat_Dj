from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('nik', 'telp', 'alamat', 'role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
