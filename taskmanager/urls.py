from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.admin_urls if hasattr(admin.site, 'admin_urls') else admin.site.urls),
    path('', include('projects.urls')),  # Inclut les URLs des projets à la racine
    path('', include('accounts.urls')),  # Inclut les URLs d'authentification
]