from django.test import TestCase

# Create your tests here.

#Test Unitario para scrape_website

from django.test import TestCase
from scraper.services.scrape import scrape_website
from unittest.mock import patch

class ScrapeWebsiteTest(TestCase):
    @patch("scraper.services.scrape.webdriver.Chrome")
    def test_scrape_website_returns_empty_list(self, mock_chrome):
        """
        Verifica que la función devuelva una lista vacía cuando no se encuentran artículos.
        """
        # Simular el comportamiento del navegador
        mock_driver = mock_chrome.return_value
        mock_driver.find_elements.return_value = []

        # Llamar a la función
        result = scrape_website(max_articles=5)

        # Verificar que se devuelve una lista vacía
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 0)

    @patch("scraper.services.scrape.webdriver.Chrome")
    def test_scrape_website_handles_exceptions(self, mock_chrome):
        """
        Verifica que la función maneje correctamente los errores al inicializar el navegador.
        """
        # Simular un error al inicializar el navegador
        mock_chrome.side_effect = Exception("Error al inicializar el navegador")

        # Llamar a la función
        result = scrape_website(max_articles=5)

        # Verificar que se devuelve una lista vacía
        self.assertEqual(result, [])



#Test Integral para scrape.py en Services
from django.test import TestCase
from scraper.services.scrape import scrape_website
from unittest.mock import patch, MagicMock

from django.test import TestCase
from scraper.services.scrape import scrape_website
from unittest.mock import patch, MagicMock

class ScrapeWebsiteIntegrationTest(TestCase):
    @patch("scraper.services.scrape.webdriver.Chrome")
    def test_scrape_website_returns_data(self, mock_chrome):
        """
        Verifica que la función devuelva datos correctamente cuando se simulan artículos.
        """
        # Simular el comportamiento del navegador
        mock_driver = mock_chrome.return_value

        # Simular un artículo
        mock_article = MagicMock()
        mock_article.find_element.side_effect = lambda by, value: MagicMock(
            text="Migraine Test Article" if value == "a.docsum-title" else "Author 1, Author 2",
            get_attribute=lambda attr: "http://integration.com" if attr == "href" else None
        )

        # Simular que el navegador encuentra un artículo
        mock_driver.find_elements.return_value = [mock_article]

        # Llamar a la función
        result = scrape_website(max_articles=1)

        # Verificar que se devuelve una lista con datos
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["title"], "Migraine Test Article")
        self.assertEqual(result[0]["source_url"], "http://integration.com")