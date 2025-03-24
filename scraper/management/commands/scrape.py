# from django.core.management.base import BaseCommand
# from scraper.services.scrape import scrape_website
# from scraper.models import ScrapedData
# import unicodedata

# class Command(BaseCommand):
#     help = "Run the web scraper"
#     # Hereda de BaseCommand, lo que permite que este comando sea ejecutable mediante python manage.py <nombre_comando>.

#     def handle(self, *args, **kwargs):
#         self.stdout.write("Iniciando el scraping...")

#         # Ejecuta la función de scraping
#         try:
#             data = scrape_website()
#             if not data:
#                 self.stdout.write(self.style.WARNING("No se encontraron datos para guardar."))
#                 return
#         except Exception as e:
#             self.stderr.write(f"Error al ejecutar el scraping: {e}")
#             return

#         # Guarda los datos en la base de datos
#         for item in data:
#             # Normaliza el título para eliminar caracteres no compatibles
#             title = item["title"] or "Sin título"
#             title = self.normalize_text(title)

#             try:
#                 ScrapedData.objects.create(title=title, url=item["url"])
#             except Exception as e:
#                 self.stderr.write(f"Error al guardar el dato: {item}. Error: {e}")

#         self.stdout.write(self.style.SUCCESS("Scraping completado con éxito."))

#     def normalize_text(self, text):
#         """
#         Normaliza el texto para eliminar caracteres no compatibles con la base de datos.
#         """
#         try:
#             # Elimina caracteres no ASCII y normaliza el texto
#             normalized_text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
#             return normalized_text
#         except Exception as e:
#             self.stderr.write(f"Error al normalizar el texto: {text}. Error: {e}")
#             return "Texto no válido"

# from django.core.management.base import BaseCommand
# from scraper.services.scrape import scrape_website
# from scraper.models import SelectedArticle  # Cambiado de core.models a scraper.models

# class Command(BaseCommand):
#     help = "Run the web scraper for PubMed"

#     def handle(self, *args, **kwargs):
#         self.stdout.write("Iniciando el scraping en PubMed...")

#         # Ejecuta la función de scraping
#         try:
#             data = scrape_website(search_term="migrañas")
#             if not data:
#                 self.stdout.write(self.style.WARNING("No se encontraron datos para guardar."))
#                 return
#         except Exception as e:
#             self.stderr.write(f"Error al ejecutar el scraping: {e}")
#             return

#         # Guarda los datos en la base de datos
#         for item in data:
#             try:
#                 SelectedArticle.objects.create(
#                     title=item["title"],
#                     authors=item["authors"],
#                     citation=item["citation"],
#                     journal=item["journal"],
#                     source_url=item["source_url"]
#                 )
#             except Exception as e:
#                 self.stderr.write(f"Error al guardar el dato: {item}. Error: {e}")

#         self.stdout.write(self.style.SUCCESS("Scraping completado con éxito."))

##############################################
#################################################
###########################################
#############################################
# from django.core.management.base import BaseCommand
# from scraper.services.scrape import scrape_website
# from scraper.models import SelectedArticle  # Cambiado de core.models a scraper.models

# class Command(BaseCommand):
#     help = "Run the web scraper for PubMed"

#     def handle(self, *args, **kwargs):
#         self.stdout.write("Iniciando el scraping en PubMed...")

#         # Preguntar al usuario cuántos artículos desea obtener
#         try:
#             max_articles = int(input("¿Cuántos artículos deseas obtener? (Ejemplo: 50): "))
#         except ValueError:
#             self.stderr.write("Por favor, ingresa un número válido.")
#             return

#         # Ejecuta la función de scraping
#         try:
#             data = scrape_website(max_articles=max_articles)
#             if not data:
#                 self.stdout.write(self.style.WARNING("No se encontraron datos para guardar."))
#                 return
#         except Exception as e:
#             self.stderr.write(f"Error al ejecutar el scraping: {e}")
#             return

#         # Guarda los datos en la base de datos
#         saved_articles = 0
#         for item in data:
#             if saved_articles >= max_articles:
#                 break
#             try:
#                 SelectedArticle.objects.create(
#                     title=item["title"],
#                     authors=item["authors"],
#                     citation=item["citation"],
#                     journal=item["journal"],
#                     source_url=item["source_url"]
#                 )
#                 saved_articles += 1
#             except Exception as e:
#                 self.stderr.write(f"Error al guardar el dato: {item}. Error: {e}")

#         self.stdout.write(self.style.SUCCESS(f"Scraping completado con éxito. Se guardaron {saved_articles} artículos."))

###################################
#######################################################
#############################################################
# from django.core.management.base import BaseCommand
# from scraper.services.scrape import scrape_website
# from scraper.models import SelectedArticle, DuplicateArticle

# class Command(BaseCommand):
#     help = "Run the web scraper for PubMed"

#     def handle(self, *args, **kwargs):
#         self.stdout.write("Iniciando el scraping en PubMed...")

#         # Preguntar al usuario cuántos artículos desea obtener
#         try:
#             max_articles = int(input("¿Cuántos artículos deseas obtener? (Ejemplo: 50): "))
#         except ValueError:
#             self.stderr.write("Por favor, ingresa un número válido.")
#             return

#         # Ejecuta la función de scraping
#         try:
#             data = scrape_website(max_articles=max_articles)
#             if not data:
#                 self.stdout.write(self.style.WARNING("No se encontraron datos para guardar."))
#                 return
#         except Exception as e:
#             self.stderr.write(f"Error al ejecutar el scraping: {e}")
#             return

#         # Guarda los datos en la base de datos
#         saved_articles = 0
#         for item in data:
#             if saved_articles >= max_articles:
#                 break
#             try:
#                 # Verificar si el artículo ya existe en la tabla principal
#                 if SelectedArticle.objects.filter(source_url=item["source_url"]).exists():
#                     # Mover a la tabla de duplicados si ya existe
#                     if not DuplicateArticle.objects.filter(source_url=item["source_url"]).exists():
#                         DuplicateArticle.objects.create(
#                             title=item["title"],
#                             authors=item["authors"],
#                             citation=item["citation"],
#                             journal=item["journal"],
#                             source_url=item["source_url"],
#                             publication_date=item["publication_date"],
#                         )
#                     continue

#                 # Guardar en la tabla principal si no es duplicado
#                 SelectedArticle.objects.create(
#                     title=item["title"],
#                     authors=item["authors"],
#                     citation=item["citation"],
#                     journal=item["journal"],
#                     source_url=item["source_url"],
#                     publication_date=item["publication_date"],
#                 )
#                 saved_articles += 1
#             except Exception as e:
#                 self.stderr.write(f"Error al guardar el dato: {item}. Error: {e}")

#         self.stdout.write(self.style.SUCCESS(f"Scraping completado con éxito. Se guardaron {saved_articles} artículos."))
################################
###########################################
########################################################


from django.core.management.base import BaseCommand
from scraper.services.scrape import scrape_website
from scraper.models import SelectedArticle, DuplicateArticle

class Command(BaseCommand):
    help = "Run the web scraper for PubMed"

    def handle(self, *args, **kwargs):
        self.stdout.write("Iniciando el scraping en PubMed...")

        # Preguntar al usuario cuántos artículos desea obtener
        try:
            max_articles = int(input("¿Cuántos artículos deseas obtener? (Ejemplo: 50): "))
        except ValueError:
            self.stderr.write("Por favor, ingresa un número válido.")
            return

        # Ejecuta la función de scraping
        try:
            data = scrape_website(max_articles=max_articles)
            if not data:
                self.stdout.write(self.style.WARNING("No se encontraron datos para guardar."))
                return
        except Exception as e:
            self.stderr.write(f"Error al ejecutar el scraping: {e}")
            return

        # Guarda los datos en la base de datos
        saved_articles = 0
        for item in data:
            print(f"Datos extraídos: {item}")  # Depuración
            if saved_articles >= max_articles:
                break
            try:
                # Verificar si el artículo ya existe en la tabla principal
                if SelectedArticle.objects.filter(source_url=item["source_url"]).exists():
                    # Mover a la tabla de duplicados si ya existe
                    if not DuplicateArticle.objects.filter(source_url=item["source_url"]).exists():
                        DuplicateArticle.objects.create(
                            title=item["title"],
                            authors=item["authors"],
                            citation=item["citation"],
                            journal=item["journal"],
                            source_url=item["source_url"],
                            publication_date=item["publication_date"],
                        )
                    continue

                # Guardar en la tabla principal si no es duplicado
                SelectedArticle.objects.create(
                    title=item["title"],
                    authors=item["authors"],
                    citation=item["citation"],
                    journal=item["journal"],
                    source_url=item["source_url"],
                    publication_date=item["publication_date"],
                )
                saved_articles += 1
            except Exception as e:
                self.stderr.write(f"Error al guardar el dato: {item}. Error: {e}")

        self.stdout.write(self.style.SUCCESS(f"Scraping completado con éxito. Se guardaron {saved_articles} artículos."))