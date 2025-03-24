# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def scrape_website():
#     """
#     Función para realizar scraping en un sitio web utilizando Selenium.
#     """
#     # Configurar opciones de Selenium
#     options = Options()
#     options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
#     options.add_argument('--no-sandbox')  # Requerido para algunos entornos
#     options.add_argument('--disable-dev-shm-usage')  # Evitar errores de memoria compartida
#     options.add_argument('--disable-gpu')  # Desactiva el uso de GPU
#     options.add_argument('--disable-software-rasterizer')  # Desactiva el rasterizador por software
#     options.add_argument('--disable-extensions')  # Desactiva extensiones
#     options.add_argument('--disable-features=VizDisplayCompositor')  # Desactiva Viz Display Compositor

#     # Inicializar el servicio de ChromeDriver
#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=options)
#     except Exception as e:
#         print(f"Error al inicializar el navegador: {e}")
#         return []

#     # Navegar al sitio web
#     url = "https://jorgebenitezlopez.com"
#     try:
#         driver.get(url)
#         print(f"Título de la página: {driver.title}")
#     except Exception as e:
#         print(f"Error al cargar la página: {e}")
#         driver.quit()
#         return []

#     # Esperar a que los elementos estén presentes
#     try:
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1"))
#         )
#         titles = driver.find_elements(By.CSS_SELECTOR, "h1")
#         urls = driver.find_elements(By.CSS_SELECTOR, "a")
#     except Exception as e:
#         print(f"Error al encontrar los elementos: {e}")
#         driver.quit()
#         return []

#     # Extraer datos
#     scraped_data = []
#     try:
#         for title, link in zip(titles, urls):
#             scraped_data.append({
#                 "title": title.text.strip(),  # Elimina espacios en blanco
#                 "url": link.get_attribute("href"),
#             })
#     except Exception as e:
#         print(f"Error al procesar los datos: {e}")

#     # Mostrar los datos extraídos para depuración
#     print("Datos extraídos:", scraped_data)

#     # Cerrar el navegador
#     driver.quit()

#     return scraped_data


###########################################################################
###########################################################################

###########################################################################
###########################################################################

###########################################################################
###########################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import urllib.parse  # Para codificar caracteres especiales en la URL

# def scrape_website(search_term="migraña"):
#     """
#     Función para realizar scraping en PubMed utilizando Selenium.
#     """
#     # Configurar opciones de Selenium
#     options = Options()
#     options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
#     options.add_argument('--no-sandbox')  # Requerido para algunos entornos
#     options.add_argument('--disable-dev-shm-usage')  # Evitar errores de memoria compartida
#     options.add_argument('--disable-gpu')  # Desactiva el uso de GPU
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.100 Safari/537.36")

#     # Inicializar el servicio de ChromeDriver
#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=options)
#     except Exception as e:
#         print(f"Error al inicializar el navegador: {e}")
#         return []

#     # Codificar el término de búsqueda para incluir caracteres especiales
#     encoded_search_term = urllib.parse.quote(search_term)

#     # Construir la URL base con el filtro de años
#     base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_search_term}&filter=datesearch.y_1&filter=years.2024-2025&page="

#     scraped_data = []

#     try:
#         page = 1
#         while True:
#             url = base_url + str(page)
#             driver.get(url)
#             print(f"Scraping página: {page}")

#             # Esperar a que los artículos estén presentes
#             WebDriverWait(driver, 20).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
#             )

#             # Extraer datos de los artículos
#             articles = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")
#             print(f"Artículos encontrados en la página {page}: {len(articles)}")

#             if not articles:
#                 break

#             for article in articles:
#                 try:
#                     title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
#                     authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
#                     citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
#                     source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")

#                     scraped_data.append({
#                         "title": title,
#                         "authors": authors,
#                         "citation": citation,
#                         "journal": "PubMed",
#                         "source_url": source_url,
#                     })
#                 except Exception as e:
#                     print(f"Error al procesar un artículo: {e}")

#             page += 1

#     except Exception as e:
#         print(f"Error durante el scraping: {e}")
#     finally:
#         driver.quit()

#     return scraped_data

###########################################################################
###########################################################################

###########################################################################
###########################################################################

###########################################################################
###########################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import urllib.parse  # Para codificar caracteres especiales en la URL

# def scrape_website(search_term="migraña"):
#     """
#     Función para realizar scraping en PubMed utilizando Selenium.
#     """
#     # Configurar opciones de Selenium
#     options = Options()
#     options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
#     options.add_argument('--no-sandbox')  # Requerido para algunos entornos
#     options.add_argument('--disable-dev-shm-usage')  # Evitar errores de memoria compartida
#     options.add_argument('--disable-gpu')  # Desactiva el uso de GPU
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
#     options.add_argument("--lang=es-ES")  # Configurar el idioma del navegador en español

#     # Inicializar el servicio de ChromeDriver
#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=options)
#     except Exception as e:
#         print(f"Error al inicializar el navegador: {e}")
#         return []

#     # Codificar el término de búsqueda para incluir caracteres especiales
#     # Aquí se asegura que "migraña" se codifique correctamente
#     encoded_search_term = urllib.parse.quote(search_term, safe='')

#     # Construir la URL base con el filtro de años
#     base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_search_term}&filter=datesearch.y_1&filter=years.2024-2025&page="

#     scraped_data = []

#     try:
#         page = 1
#         while True:
#             url = base_url + str(page)
#             driver.get(url)
#             print(f"Scraping página: {page}")

#             # Esperar a que los artículos estén presentes
#             WebDriverWait(driver, 20).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
#             )

#             # Extraer datos de los artículos
#             articles = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")
#             print(f"Artículos encontrados en la página {page}: {len(articles)}")

#             if not articles:
#                 break

#             for article in articles:
#                 try:
#                     title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
#                     authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
#                     citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
#                     source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")

#                     scraped_data.append({
#                         "title": title,
#                         "authors": authors,
#                         "citation": citation,
#                         "journal": "PubMed",
#                         "source_url": source_url,
#                     })
#                 except Exception as e:
#                     print(f"Error al procesar un artículo: {e}")

#             page += 1

#     except Exception as e:
#         print(f"Error durante el scraping: {e}")
#     finally:
#         driver.quit()

#     return scraped_data


###########################################################################
###########################################################################

###########################################################################
###########################################################################

###########################################################################
###########################################################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import urllib.parse  # Para codificar caracteres especiales en la URL

# def scrape_website(max_articles=50):
#     """
#     Función para realizar scraping en PubMed utilizando Selenium.
#     Siempre busca la palabra "migraine".
#     """
#     # Configurar opciones de Selenium
#     options = Options()
#     options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
#     options.add_argument('--no-sandbox')  # Requerido para algunos entornos
#     options.add_argument('--disable-dev-shm-usage')  # Evitar errores de memoria compartida
#     options.add_argument('--disable-gpu')  # Desactiva el uso de GPU
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
#     options.add_argument("--lang=en-US")  # Configurar el idioma del navegador en inglés

#     # Inicializar el servicio de ChromeDriver
#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=options)
#     except Exception as e:
#         print(f"Error al inicializar el navegador: {e}")
#         return []

#     # Construir la URL base con la palabra "migraine"
#     search_term = "migraine"
#     encoded_search_term = urllib.parse.quote(search_term, safe='')
#     base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_search_term}&filter=datesearch.y_1&page="

#     scraped_data = []
#     total_articles = 0

#     try:
#         page = 1
#         while total_articles < max_articles:
#             url = base_url + str(page)
#             driver.get(url)
#             print(f"Scraping página: {page}")

#             # Esperar a que los artículos estén presentes
#             WebDriverWait(driver, 20).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
#             )

#             # Extraer datos de los artículos
#             articles = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")
#             print(f"Artículos encontrados en la página {page}: {len(articles)}")

#             if not articles:
#                 break

#             for article in articles:
#                 if total_articles >= max_articles:
#                     break
#                 try:
#                     title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
#                     # Validar que el título contenga la palabra "migraine"
#                     if "migraine" not in title.lower():
#                         continue

#                     authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
#                     citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
#                     source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")

#                     scraped_data.append({
#                         "title": title,
#                         "authors": authors,
#                         "citation": citation,
#                         "journal": "PubMed",
#                         "source_url": source_url,
#                     })
#                     total_articles += 1
#                 except Exception as e:
#                     print(f"Error al procesar un artículo: {e}")

#             page += 1

#     except Exception as e:
#         print(f"Error durante el scraping: {e}")
#     finally:
#         driver.quit()

#     return scraped_data

#####################################################################
####################################
########################################################################
################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import urllib.parse  # Para codificar caracteres especiales en la URL
# from datetime import datetime  # Para formatear fechas

# def scrape_website(max_articles=50):
#     """
#     Función para realizar scraping en PubMed utilizando Selenium.
#     Siempre busca la palabra "migraine".
#     """
#     # Configurar opciones de Selenium
#     options = Options()
#     options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
#     options.add_argument('--no-sandbox')  # Requerido para algunos entornos
#     options.add_argument('--disable-dev-shm-usage')  # Evitar errores de memoria compartida
#     options.add_argument('--disable-gpu')  # Desactiva el uso de GPU
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
#     options.add_argument("--lang=en-US")  # Configurar el idioma del navegador en inglés

#     # Inicializar el servicio de ChromeDriver
#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=options)
#     except Exception as e:
#         print(f"Error al inicializar el navegador: {e}")
#         return []

#     # Construir la URL base con la palabra "migraine"
#     search_term = "migraine"
#     encoded_search_term = urllib.parse.quote(search_term, safe='')
#     base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_search_term}&filter=datesearch.y_1&page="

#     scraped_data = []
#     total_articles = 0

#     try:
#         page = 1
#         while total_articles < max_articles:
#             url = base_url + str(page)
#             driver.get(url)
#             print(f"Scraping página: {page}")

#             # Esperar a que los artículos estén presentes
#             WebDriverWait(driver, 20).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
#             )

#             # Extraer datos de los artículos
#             articles = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")
#             print(f"Artículos encontrados en la página {page}: {len(articles)}")

#             if not articles:
#                 break

#             for article in articles:
#                 if total_articles >= max_articles:
#                     break
#                 try:
#                     title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
#                     # Validar que el título contenga la palabra "migraine"
#                     if "migraine" not in title.lower():
#                         continue

#                     authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
#                     citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
#                     source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")

#                     # Extraer y formatear la fecha de publicación
#                     try:
#                         raw_date = article.find_element(By.CSS_SELECTOR, "span.citation-part").text.strip()
#                         # Intentar convertir la fecha al formato YYYY-MM-DD
#                         publication_date = datetime.strptime(raw_date, "%Y %b %d").date()
#                     except Exception as e:
#                         print(f"Error al procesar la fecha de publicación: {e}")
#                         publication_date = None  # Si no se puede extraer, dejar como None

#                     scraped_data.append({
#                         "title": title,
#                         "authors": authors,
#                         "citation": citation,
#                         "journal": "PubMed",
#                         "source_url": source_url,
#                         "publication_date": publication_date,
#                     })
#                     total_articles += 1
#                 except Exception as e:
#                     print(f"Error al procesar un artículo: {e}")

#             page += 1

#     except Exception as e:
#         print(f"Error durante el scraping: {e}")
#     finally:
#         driver.quit()

#     return scraped_data

#####################
##################################
#############################################

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import urllib.parse  # Para codificar caracteres especiales en la URL
# from datetime import datetime  # Para formatear fechas
# import re  # Para buscar patrones en el texto

# def scrape_website(max_articles=50):
#     """
#     Función para realizar scraping en PubMed utilizando Selenium.
#     Siempre busca la palabra "migraine".
#     """
#     # Configurar opciones de Selenium
#     options = Options()
#     options.add_argument('--headless')  # Ejecutar en modo headless (sin interfaz gráfica)
#     options.add_argument('--no-sandbox')  # Requerido para algunos entornos
#     options.add_argument('--disable-dev-shm-usage')  # Evitar errores de memoria compartida
#     options.add_argument('--disable-gpu')  # Desactiva el uso de GPU
#     options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0")
#     options.add_argument("--lang=en-US")  # Configurar el idioma del navegador en inglés

#     # Inicializar el servicio de ChromeDriver
#     try:
#         service = Service(ChromeDriverManager().install())
#         driver = webdriver.Chrome(service=service, options=options)
#     except Exception as e:
#         print(f"Error al inicializar el navegador: {e}")
#         return []

#     # Construir la URL base con la palabra "migraine"
#     search_term = "migraine"
#     encoded_search_term = urllib.parse.quote(search_term, safe='')
#     base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_search_term}&filter=datesearch.y_1&page="

#     scraped_data = []
#     total_articles = 0

#     try:
#         page = 1
#         while total_articles < max_articles:
#             url = base_url + str(page)
#             driver.get(url)
#             print(f"Scraping página: {page}")

#             # Esperar a que los artículos estén presentes
#             WebDriverWait(driver, 20).until(
#                 EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
#             )

#             # Extraer datos de los artículos
#             articles = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")
#             print(f"Artículos encontrados en la página {page}: {len(articles)}")

#             if not articles:
#                 break

#             for article in articles:
#                 if total_articles >= max_articles:
#                     break
#                 try:
#                     # Extraer el título
#                     title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
#                     print(f"Título extraído: {title}")  # Depuración
#                     if "migraine" not in title.lower():
#                         print("El título no contiene la palabra 'migraine'. Se omite.")
#                         continue

#                     # Extraer los autores
#                     authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
#                     print(f"Autores extraídos: {authors}")  # Depuración

#                     # Extraer la cita
#                     citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
#                     print(f"Citación extraída: {citation}")  # Depuración

#                     # Extraer la URL
#                     source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")
#                     print(f"URL extraída: {source_url}")  # Depuración

#                     # Extraer y formatear la fecha de publicación
#                     try:
#                         raw_date_text = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
#                         print(f"Texto de la fecha extraído: {raw_date_text}")  # Depuración
#                         match = re.search(r"Publicación electrónica (\d{1,2} de \w+ de \d{4})", raw_date_text)
#                         if match:
#                             raw_date = match.group(1)
#                             publication_date = datetime.strptime(raw_date, "%d de %B de %Y").date()
#                         else:
#                             publication_date = None
#                     except Exception as e:
#                         print(f"Error al procesar la fecha de publicación: {e}")
#                         publication_date = None

#                     # Agregar los datos extraídos a la lista
#                     scraped_data.append({
#                         "title": title,
#                         "authors": authors,
#                         "citation": citation,
#                         "journal": "PubMed",
#                         "source_url": source_url,
#                         "publication_date": publication_date,
#                     })
#                     total_articles += 1
#                 except Exception as e:
#                     print(f"Error al procesar un artículo: {e}")

#             page += 1

#     except Exception as e:
#         print(f"Error durante el scraping: {e}")
#     finally:
#         driver.quit()

#     return scraped_data

##############################
########################################
#################################################
#############################################################
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

def scrape_website(max_articles=50):
    """
    Función para realizar scraping en PubMed utilizando Selenium.
    Siempre busca la palabra "migraine".
    """
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
        print(f"Error al inicializar el navegador: {e}")
        return []

    # Construir la URL base con la palabra "migraine"
    search_term = "migraine"
    encoded_search_term = urllib.parse.quote(search_term, safe='')
    base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_search_term}&filter=datesearch.y_1&page="

    scraped_data = []
    total_articles = 0

    try:
        page = 1
        while total_articles < max_articles:
            url = base_url + str(page)
            driver.get(url)
            print(f"Scraping página: {page}")

            # Esperar a que los artículos estén presentes
            WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
            )

            # Extraer datos de los artículos
            articles = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")
            print(f"Artículos encontrados en la página {page}: {len(articles)}")

            if not articles:
                break

            for article in articles:
                if total_articles >= max_articles:
                    break
                try:
                    # Extraer el título
                    title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
                    print(f"Título extraído: {title}")  # Depuración
                    if "migraine" not in title.lower():
                        print("El título no contiene la palabra 'migraine'. Se omite.")
                        continue

                    # Extraer los autores
                    authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
                    print(f"Autores extraídos: {authors}")  # Depuración

                    # Extraer la cita
                    citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
                    print(f"Citación extraída: {citation}")  # Depuración

                    # Extraer la URL
                    source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")
                    print(f"URL extraída: {source_url}")  # Depuración

                    # Extraer la fecha de publicación desde la cita
                    try:
                        # Buscar un patrón de fecha en la cita (formato: "2024 Jul 5")
                        match = re.search(r"(\d{4} \w{3} \d{1,2})", citation)
                        if match:
                            raw_date = match.group(1)
                            publication_date = datetime.strptime(raw_date, "%Y %b %d").date()
                        else:
                            publication_date = None
                    except Exception as e:
                        print(f"Error al procesar la fecha de publicación: {e}")
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
                    print(f"Error al procesar un artículo: {e}")

            page += 1

    except Exception as e:
        print(f"Error durante el scraping: {e}")
    finally:
        driver.quit()

    return scraped_data