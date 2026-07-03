from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Projet, Tache

class ProjectAndTaskTests(TestCase):

    def setUp(self):
        # Configuration initiale : création d'un utilisateur et d'un client de test
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Création d'un projet de test
        self.projet = Projet.objects.create(
            nom="Projet Test DevOps",
            description="Description de test",
            createur=self.user
        )

    def test_projet_creation(self):
        # Vérifie que le projet a bien été créé en base de données
        self.assertEqual(self.projet.nom, "Projet Test DevOps")
        self.assertEqual(self.projet.createur.username, "testuser")

    def test_dashboard_access_logged_in(self):
        # Vérifie qu'un utilisateur connecté peut accéder au tableau de bord
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_access_anonymous(self):
        # Vérifie qu'un utilisateur non connecté est redirigé vers la page de connexion
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)  # 302 = Redirection

    def test_tache_creation_default_status(self):
        # Vérifie qu'une tâche est créée avec le statut 'todo' par défaut
        tache = Tache.objects.create(
            titre="Vérifier le pipeline",
            projet=self.projet
        )
        self.assertEqual(tache.statut, 'todo')