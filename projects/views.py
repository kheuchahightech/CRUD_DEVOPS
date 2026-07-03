from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Projet, Tache
from django.contrib.auth.models import User

@login_required
def dashboard(request):
    # Affiche les projets dont l'utilisateur est créateur ou membre
    projets = Projet.objects.filter(createur=request.user) | Projet.objects.filter(membres=request.user)
    return render(request, 'projects/dashboard.html', {'projets': projets.distinct()})

@login_required
def projet_detail(request, id):
    projet = get_object_or_404(Projet, id=id)
    taches = projet.taches.all()
    return render(request, 'projects/projet_detail.html', {'projet': projet, 'taches': taches})

@login_required
def projet_create(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        description = request.POST.get('description')
        if nom:
            projet = Projet.objects.create(nom=nom, description=description, createur=request.user)
            return redirect('dashboard')
    return render(request, 'projects/projet_form.html')

@login_required
def tache_create(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        description = request.POST.get('description')
        projet_id = request.POST.get('projet')
        projet = get_object_or_404(Projet, id=projet_id)
        
        if titre:
            Tache.objects.create(
                titre=titre,
                description=description,
                projet=projet,
                statut='todo'
            )
            return redirect('projet_detail', id=projet.id)
            
    projets = Projet.objects.filter(createur=request.user) | Projet.objects.filter(membres=request.user)
    return render(request, 'projects/tache_form.html', {'projets': projets.distinct()})