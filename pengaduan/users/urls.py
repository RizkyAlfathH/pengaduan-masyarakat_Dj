from django.urls import path
from .views import user_list, user_create, user_edit, user_delete
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('laporan/', views.laporan_view, name='laporan'),
    path('users/', user_list, name='user_list'),
    path('users/create/', user_create, name='user_create'),
    path('users/edit/<int:user_id>/', user_edit, name='user_edit'),
    path('users/delete/<int:user_id>/', user_delete, name='user_delete'),
]
