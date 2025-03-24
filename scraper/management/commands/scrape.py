import logging
from django.core.management.base import BaseCommand
from scraper.services.scrape import scrape_website
from scraper.models import SelectedArticle, DuplicateArticle

# Configurar el logger
logger = logging.getLogger('scraper')

class Command(BaseCommand):
    help = "Ejecuta el scraper para extraer datos de PubMed."

    def handle(self, *args, **kwargs):
        logger.info("Iniciando el comando de scraping...")

        # Preguntar al usuario la palabra clave
        search_term = input("¿Qué palabra deseas buscar en PubMed? (Por defecto: 'migraine'): ") or "migraine"

        # Preguntar al usuario cuántos artículos desea scrapear
        try:
            max_articles = int(input("¿Cuántos artículos deseas scrapear? (Por defecto: 50): ") or 50)
        except ValueError:
            logger.error("Entrada inválida. Usando el valor por defecto: 50.")
            max_articles = 50

        try:
            # Llamar a la función de scraping con los parámetros proporcionados
            scraped_data = scrape_website(search_term=search_term, max_articles=max_articles)

            for data in scraped_data:
                # Verificar si el artículo ya existe en la base de datos
                if SelectedArticle.objects.filter(source_url=data["source_url"]).exists():
                    logger.warning(f"Artículo duplicado detectado: {data['title']}")
                    # Evitar duplicados en DuplicateArticle
                    DuplicateArticle.objects.get_or_create(
                        title=data["title"],
                        authors=data["authors"],
                        citation=data["citation"],
                        journal=data["journal"],
                        source_url=data["source_url"],
                        publication_date=data["publication_date"],
                    )
                else:
                    # Crear un nuevo artículo en la base de datos
                    SelectedArticle.objects.create(
                        title=data["title"],
                        authors=data["authors"],
                        citation=data["citation"],
                        journal=data["journal"],
                        source_url=data["source_url"],
                        publication_date=data["publication_date"],
                    )

            logger.info(f"Scraping completado. Total de artículos extraídos: {len(scraped_data)}")
        except Exception as e:
            logger.error(f"Error durante la ejecución del comando scrape: {e}", exc_info=True)
            raise