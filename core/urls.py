from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('superuser/', views.admin_dashboard, name='admin_dashboard'),
    path('events/', views.events_page, name='events'),
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('events/<int:event_id>/brochure/', views.download_brochure, name='download_brochure'),
]
