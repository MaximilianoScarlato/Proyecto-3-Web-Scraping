from django.test import TestCase

# Create your tests here.

#Test Unitario para SelectedArticleForm y DuplicateArticleForm

from django.test import TestCase
from scraper.forms import SelectedArticleForm, DuplicateArticleForm
from scraper.models import SelectedArticle, DuplicateArticle

class SelectedArticleFormTest(TestCase):
    def test_valid_form(self):
        data = {
            "title": "Test Article",
            "authors": "Author 1, Author 2",
            "citation": "Test Citation",
            "journal": "Test Journal",
            "source_url": "http://example.com",
            "publication_date": "2025-01-01",
        }
        form = SelectedArticleForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            "title": "",  # Campo requerido vacío
            "authors": "Author 1, Author 2",
            "citation": "Test Citation",
            "journal": "Test Journal",
            "source_url": "http://example.com",
            "publication_date": "2025-01-01",
        }
        form = SelectedArticleForm(data=data)
        self.assertFalse(form.is_valid())

class DuplicateArticleFormTest(TestCase):
    def test_valid_form(self):
        data = {
            "title": "Duplicate Article",
            "authors": "Author 1, Author 2",
            "citation": "Duplicate Citation",
            "journal": "Duplicate Journal",
            "source_url": "http://duplicate.com",
            "publication_date": "2025-01-01",
        }
        form = DuplicateArticleForm(data=data)
        self.assertTrue(form.is_valid())


#1. Test Integral para Forms
from django.test import TestCase
from scraper.forms import SelectedArticleForm, DuplicateArticleForm
from scraper.models import SelectedArticle, DuplicateArticle

class SelectedArticleFormIntegrationTest(TestCase):
    def test_form_saves_valid_data(self):
        data = {
            "title": "Integration Test Article",
            "authors": "Author 1, Author 2",
            "citation": "Integration Citation",
            "journal": "Integration Journal",
            "source_url": "http://integration.com",
            "publication_date": "2025-01-01",
        }
        form = SelectedArticleForm(data=data)
        self.assertTrue(form.is_valid())
        article = form.save()
        self.assertEqual(article.title, "Integration Test Article")
        self.assertEqual(SelectedArticle.objects.count(), 1)

class DuplicateArticleFormIntegrationTest(TestCase):
    def test_form_saves_valid_data(self):
        data = {
            "title": "Duplicate Integration Article",
            "authors": "Author 3, Author 4",
            "citation": "Duplicate Integration Citation",
            "journal": "Duplicate Integration Journal",
            "source_url": "http://duplicate-integration.com",
            "publication_date": "2025-01-02",
        }
        form = DuplicateArticleForm(data=data)
        self.assertTrue(form.is_valid())
        article = form.save()
        self.assertEqual(article.title, "Duplicate Integration Article")
        self.assertEqual(DuplicateArticle.objects.count(), 1)