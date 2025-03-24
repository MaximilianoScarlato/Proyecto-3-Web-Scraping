from django.test import TestCase
from django.urls import reverse
from scraper.models import SelectedArticle, DuplicateArticle
from django.contrib.auth.models import User

class SelectedArticleViewsTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Crear un artículo de prueba en la base de datos
        self.article = SelectedArticle.objects.create(
            title="Test Article",
            authors="Author 1, Author 2",
            citation="Test Citation",
            journal="Test Journal",
            source_url="http://example.com",
            publication_date="2025-01-01"
        )

    def test_home_view(self):
        """Prueba que la vista de inicio se carga correctamente."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scraper/home.html')

    def test_selected_article_list_view(self):
        """Prueba que la lista de artículos seleccionados se carga correctamente."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.get(reverse('selected_article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")

    def test_selected_article_create_view(self):
        """Prueba que se puede crear un artículo seleccionado."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.post(reverse('selected_article_create'), {
            'title': "New Article",
            'authors': "Author 3",
            'citation': "New Citation",
            'journal': "New Journal",
            'source_url': "http://newexample.com",
            'publication_date': "2025-02-01"
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras crear
        self.assertTrue(SelectedArticle.objects.filter(title="New Article").exists())

    def test_selected_article_update_view(self):
        """Prueba que se puede actualizar un artículo seleccionado."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.post(reverse('selected_article_update', args=[self.article.id]), {
            'title': "Updated Article",
            'authors': "Updated Author",
            'citation': "Updated Citation",
            'journal': "Updated Journal",
            'source_url': "http://example.com",
            'publication_date': "2025-01-02"
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras actualizar
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, "Updated Article")

    def test_selected_article_delete_view(self):
        """Prueba que se puede eliminar un artículo seleccionado."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.post(reverse('selected_article_delete', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)  # Redirección tras eliminar
        self.assertFalse(SelectedArticle.objects.filter(id=self.article.id).exists())

class DuplicateArticleViewsTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Crear un artículo duplicado de prueba en la base de datos
        self.duplicate_article = DuplicateArticle.objects.create(
            title="Duplicate Test Article",
            authors="Author 1, Author 2",
            citation="Duplicate Test Citation",
            journal="Duplicate Test Journal",
            source_url="http://duplicate.com",
            publication_date="2025-01-01"
        )

    def test_duplicate_article_list_view(self):
        """Prueba que la lista de artículos duplicados se carga correctamente."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.get(reverse('duplicate_article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Duplicate Test Article")


# Test de Integración para las Vistas en views.py
class SelectedArticleIntegrationTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Crear un artículo de prueba en la base de datos
        self.article = SelectedArticle.objects.create(
            title="Test Article",
            authors="Author 1, Author 2",
            citation="Test Citation",
            journal="Test Journal",
            source_url="http://example.com",
            publication_date="2025-01-01"
        )

    def test_home_view_integration(self):
        """Prueba que la vista de inicio se carga correctamente."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'scraper/home.html')

    def test_selected_article_list_view_integration(self):
        """Prueba que la lista de artículos seleccionados muestra los datos correctamente."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.get(reverse('selected_article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Article")

    def test_selected_article_create_view_integration(self):
        """Prueba que se puede crear un artículo seleccionado."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.post(reverse('selected_article_create'), {
            'title': "Integration Article",
            'authors': "Author 3",
            'citation': "Integration Citation",
            'journal': "Integration Journal",
            'source_url': "http://integration.com",
            'publication_date': "2025-02-01"
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras crear
        self.assertTrue(SelectedArticle.objects.filter(title="Integration Article").exists())

    def test_selected_article_update_view_integration(self):
        """Prueba que se puede actualizar un artículo seleccionado."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.post(reverse('selected_article_update', args=[self.article.id]), {
            'title': "Updated Integration Article",
            'authors': "Updated Author",
            'citation': "Updated Citation",
            'journal': "Updated Journal",
            'source_url': "http://example.com",
            'publication_date': "2025-02-02"
        })
        self.assertEqual(response.status_code, 302)  # Redirección tras actualizar
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, "Updated Integration Article")

    def test_selected_article_delete_view_integration(self):
        """Prueba que se puede eliminar un artículo seleccionado."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.post(reverse('selected_article_delete', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)  # Redirección tras eliminar
        self.assertFalse(SelectedArticle.objects.filter(id=self.article.id).exists())

class DuplicateArticleIntegrationTest(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Crear un artículo duplicado de prueba en la base de datos
        self.duplicate_article = DuplicateArticle.objects.create(
            title="Duplicate Test Article",
            authors="Author 1, Author 2",
            citation="Duplicate Test Citation",
            journal="Duplicate Test Journal",
            source_url="http://duplicate.com",
            publication_date="2025-01-01"
        )

    def test_duplicate_article_list_view_integration(self):
        """Prueba que la lista de artículos duplicados muestra los datos correctamente."""
        self.client.login(username='testuser', password='testpassword')  # Autenticar al usuario
        response = self.client.get(reverse('duplicate_article_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Duplicate Test Article")