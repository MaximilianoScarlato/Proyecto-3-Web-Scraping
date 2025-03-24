from django.test import TestCase

# Create your tests here.

#Test Unitario para SelectedArticle y DuplicateArticle

from django.test import TestCase
from scraper.models import SelectedArticle, DuplicateArticle

class SelectedArticleModelTest(TestCase):
    def setUp(self):
        self.article = SelectedArticle.objects.create(
            title="Test Article",
            authors="Author 1, Author 2",
            citation="Test Citation",
            journal="Test Journal",
            source_url="http://example.com",
            publication_date="2025-01-01"
        )

    def test_str_representation(self):
        self.assertEqual(str(self.article), "Test Article")

    def test_unique_source_url(self):
        with self.assertRaises(Exception):
            SelectedArticle.objects.create(
                title="Duplicate Article",
                authors="Author 3",
                citation="Duplicate Citation",
                journal="Duplicate Journal",
                source_url="http://example.com",  # URL duplicada
                publication_date="2025-01-02"
            )

class DuplicateArticleModelTest(TestCase):
    def setUp(self):
        self.duplicate_article = DuplicateArticle.objects.create(
            title="Duplicate Article",
            authors="Author 1, Author 2",
            citation="Duplicate Citation",
            journal="Duplicate Journal",
            source_url="http://duplicate.com",
            publication_date="2025-01-01"
        )

    def test_str_representation(self):
        self.assertEqual(str(self.duplicate_article), "Duplicate Article")
        
        

#Test de Integración para SelectedArticle y DuplicateArticle


from django.test import TestCase
from scraper.models import SelectedArticle, DuplicateArticle

class ArticleIntegrationTest(TestCase):
    def test_create_and_retrieve_articles(self):
        # Crear un artículo en SelectedArticle
        selected_article = SelectedArticle.objects.create(
            title="Integration Test Article",
            authors="Author 1, Author 2",
            citation="Integration Citation",
            journal="Integration Journal",
            source_url="http://integration.com",
            publication_date="2025-01-01"
        )

        # Verificar que se puede recuperar correctamente
        retrieved_article = SelectedArticle.objects.get(source_url="http://integration.com")
        self.assertEqual(retrieved_article.title, "Integration Test Article")

        # Crear un artículo duplicado en DuplicateArticle
        duplicate_article = DuplicateArticle.objects.create(
            title="Duplicate Integration Article",
            authors="Author 3, Author 4",
            citation="Duplicate Integration Citation",
            journal="Duplicate Integration Journal",
            source_url="http://duplicate-integration.com",
            publication_date="2025-01-02"
        )

        # Verificar que se puede recuperar correctamente
        retrieved_duplicate = DuplicateArticle.objects.get(source_url="http://duplicate-integration.com")
        self.assertEqual(retrieved_duplicate.title, "Duplicate Integration Article")
