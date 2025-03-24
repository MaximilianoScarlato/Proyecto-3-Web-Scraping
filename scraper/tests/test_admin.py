

# Create your tests here.

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from scraper.models import SelectedArticle, DuplicateArticle
from scraper.admin import SelectedArticleAdmin, DuplicateArticleAdmin
from django.contrib.admin.sites import site

# Test Unitario para SelectedArticleAdmin y DuplicateArticleAdmin
class AdminTest(TestCase):
    def test_selected_article_admin_registered(self):
        self.assertIn(SelectedArticle, site._registry)
        self.assertIsInstance(site._registry[SelectedArticle], SelectedArticleAdmin)

    def test_duplicate_article_admin_registered(self):
        self.assertIn(DuplicateArticle, site._registry)
        self.assertIsInstance(site._registry[DuplicateArticle], DuplicateArticleAdmin)

# Test de Integración para Admin
class AdminIntegrationTest(TestCase):
    def setUp(self):
        # Crear un usuario administrador para autenticación
        self.admin_user = User.objects.create_superuser(
            username="admin",
            password="adminpassword",
            email="admin@example.com"
        )
        self.client.login(username="admin", password="adminpassword")

        # Crear un artículo de prueba
        self.article = SelectedArticle.objects.create(
            title="Admin Test Article",
            authors="Author 1, Author 2",
            citation="Admin Citation",
            journal="Admin Journal",
            source_url="http://admin.com",
            publication_date="2025-01-01"
        )

    def test_admin_list_view(self):
        # Verificar que la vista de lista del administrador carga correctamente
        response = self.client.get(reverse('admin:scraper_selectedarticle_changelist'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Admin Test Article")

    def test_admin_add_view(self):
        # Verificar que la vista de agregar del administrador carga correctamente
        response = self.client.get(reverse('admin:scraper_selectedarticle_add'))
        self.assertEqual(response.status_code, 200)