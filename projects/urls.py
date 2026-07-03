from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('projet/<int:id>/', views.projet_detail, name='projet_detail'),
    path('projet/creer/', views.projet_create, name='projet_create'),
    path('tache/creer/', views.tache_create, name='tache_create'),
]