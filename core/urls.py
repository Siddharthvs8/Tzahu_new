from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('superuser/', views.admin_dashboard, name='admin_dashboard'),
]
