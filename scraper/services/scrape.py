import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse  # Para codificar caracteres especiales en la URL
from datetime import datetime  # Para formatear fechas
import re  # Para buscar patrones en el texto

# Configurar el logger
logger = logging.getLogger('scraper')
logger.setLevel(logging.DEBUG)  # Cambiar a INFO en producción

# Configurar el handler para archivo
file_handler = logging.FileHandler('scraper.log')
file_handler.setLevel(logging.DEBUG)  # Cambiar a INFO en producción

# Configurar el handler para consola
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formato de los logs
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Agregar handlers al logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def scrape_website(search_term="migraine", max_articles=50):
    """
    Función para realizar scraping en PubMed utilizando Selenium.
    Busca la palabra clave proporcionada por el usuario.
    """
    logger.info(f"Iniciando el scraping en PubMed con la palabra clave: {search_term}")

    # Configurar opciones de Selenium
    options = Options()
    options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
    options.add_argument('--no-sandbox')  # Requerido para algunos entornos
    options.add_argument('--disable-dev-shm-usage')  # Evitar errores de memoria compartida
    options.add_argument('--disable-gpu')  # Desactiva el uso de GPU
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
    options.add_argument("--lang=en-US")  # Configurar el idioma del navegador en inglés

    # Inicializar el servicio de ChromeDriver
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    except Exception as e:
        logger.error(f"Error al inicializar el navegador: {e}", exc_info=True)
        return []

    # Construir la URL base con la palabra clave proporcionada
    encoded_search_term = urllib.parse.quote(search_term, safe='')
    base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_search_term}&filter=datesearch.y_1&page="

    scraped_data = []
    total_articles = 0

    try:
        page = 1
        while total_articles < max_articles:
            url = base_url + str(page)
            driver.get(url)
            logger.info(f"Scraping página: {page}")

            # Esperar a que los artículos estén presentes
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
            )

            # Extraer datos de los artículos
            articles = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")
            logger.info(f"Artículos encontrados en la página {page}: {len(articles)}")

            if not articles:
                logger.warning("No se encontraron más artículos en la página.")
                break

            for article in articles:
                if total_articles >= max_articles:
                    logger.info("Se alcanzó el límite máximo de artículos.")
                    break
                try:
                    # Extraer el título
                    title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
                    logger.debug(f"Título extraído: {title}")
                    if search_term.lower() not in title.lower():
                        logger.debug(f"El título no contiene la palabra '{search_term}'. Se omite.")
                        continue

                    # Extraer los autores
                    authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
                    logger.debug(f"Autores extraídos: {authors}")

                    # Extraer la cita
                    citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
                    logger.debug(f"Citación extraída: {citation}")

                    # Extraer la URL
                    source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")
                    logger.debug(f"URL extraída: {source_url}")

                    # Extraer la fecha de publicación desde la cita
                    try:
                        match = re.search(r"(\d{4} \w{3} \d{1,2})", citation)
                        if match:
                            raw_date = match.group(1)
                            publication_date = datetime.strptime(raw_date, "%Y %b %d").date()
                        else:
                            publication_date = None
                    except Exception as e:
                        logger.error(f"Error al procesar la fecha de publicación: {e}", exc_info=True)
                        publication_date = None

                    # Agregar los datos extraídos a la lista
                    scraped_data.append({
                        "title": title,
                        "authors": authors,
                        "citation": citation,
                        "journal": "PubMed",
                        "source_url": source_url,
                        "publication_date": publication_date,
                    })
                    total_articles += 1
                except Exception as e:
                    logger.error(f"Error al procesar un artículo: {e}", exc_info=True)

            page += 1

    except Exception as e:
        logger.error(f"Error durante el scraping: {e}", exc_info=True)
    finally:
        driver.quit()
        logger.info("Scraping completado.")

    return scraped_data