from django.test import TestCase
from django.core.management import call_command
from scraper.models import SelectedArticle, DuplicateArticle
from unittest.mock import patch

class ScrapeCommandTest(TestCase):
    @patch("scraper.management.commands.scrape.scrape_website")
    def test_scrape_command(self, mock_scrape_website):
        # Simular datos de scraping
        mock_scrape_website.return_value = [
            {
                "title": "Test Article",
                "authors": "Author 1, Author 2",
                "citation": "Test Citation",
                "journal": "Test Journal",
                "source_url": "http://example.com",
                "publication_date": "2025-01-01",
            }
        ]

        # Ejecutar el comando
        call_command("scrape")

        # Verificar que los datos se guardaron en la base de datos
        self.assertEqual(SelectedArticle.objects.count(), 1)
        article = SelectedArticle.objects.first()
        self.assertEqual(article.title, "Test Article")
        self.assertEqual(article.source_url, "http://example.com")


class ScrapeCommandIntegrationTest(TestCase):
    @patch("scraper.management.commands.scrape.scrape_website")
    def test_scrape_command_saves_data(self, mock_scrape_website):
        """
        Verifica que el comando scrape guarde correctamente los datos en la base de datos.
        """
        # Simular datos de scraping
        mock_scrape_website.return_value = [
            {
                "title": "Integration Test Article",
                "authors": "Author 1, Author 2",
                "citation": "Integration Citation",
                "journal": "Integration Journal",
                "source_url": "http://integration.com",
                "publication_date": "2025-01-01",
            },
            {
                "title": "Integration Test Article",  # Artículo duplicado
                "authors": "Author 1, Author 2",
                "citation": "Integration Citation",
                "journal": "Integration Journal",
                "source_url": "http://integration.com",  # URL duplicada
                "publication_date": "2025-01-01",
            },
        ]

        # Ejecutar el comando
        call_command("scrape")

        # Verificar que solo se guardó 1 artículo en SelectedArticle
        self.assertEqual(SelectedArticle.objects.count(), 1)

        # Verificar que el artículo duplicado se guardó en DuplicateArticle
        self.assertEqual(DuplicateArticle.objects.count(), 1)

        # Verificar los datos del artículo principal
        article = SelectedArticle.objects.first()
        self.assertEqual(article.title, "Integration Test Article")
        self.assertEqual(article.source_url, "http://integration.com")

        # Verificar los datos del artículo duplicado
        duplicate = DuplicateArticle.objects.first()
        self.assertEqual(duplicate.title, "Integration Test Article")
        self.assertEqual(duplicate.source_url, "http://integration.com")