# Web Scraper Fusion

## 📌 Índice
- [📝 Sobre el Proyecto](#sobre-el-proyecto)
- [⚡ Características principales](#características-principales)
- [⛔ Temas actuales](#temas-actuales)
- [🔧 Posibles mejoras](#posibles-mejoras)
- [👨‍💻 Tecnologías utilizadas](#tecnologías-utilizadas)
- [⚙ Instalación y uso](#instalación-y-uso)
- [📂 Estructura de la carpeta](#estructura-de-la-carpeta)
- [🧪 Realización de pruebas](#realización-de-pruebas)
- [🌟 Estado del proyecto](#estado-del-proyecto)

## 📝 Sobre el Proyecto
Web Scraper Fusion es un sistema backend desarrollado con Django y MySQL que permite realizar búsquedas en PubMed, guardar artículos seleccionados y gestionar artículos duplicados. El objetivo principal es facilitar la recopilación y organización de información científica.

El sistema incluye las siguientes funcionalidades:
- Búsqueda de artículos en PubMed.
- Gestión de artículos seleccionados.
- Registro de artículos duplicados.
- Acceso directo a los enlaces de los artículos.

El proyecto sigue la metodología Scrum y está organizado en GitHub. Incluye pruebas unitarias para garantizar la confiabilidad del código.

## ⚡ Características principales
- ✅ Búsqueda de artículos en PubMed utilizando Selenium.
- ✅ Gestión de artículos seleccionados y duplicados.
- ✅ Columna "Seleccionar enlace" para acceder directamente a los artículos.
- ✅ Manejo de excepciones para artículos duplicados.
- ✅ Base de datos estructurada con las siguientes tablas:
  - `SelectedArticle`: Artículos seleccionados.
  - `DuplicateArticle`: Artículos duplicados.
- ✅ Uso de sesiones para almacenar temporalmente los resultados de búsqueda.
- ✅ Interfaz de usuario con Bootstrap para una experiencia amigable.
- ✅ Scripts para creación de bases de datos y migración de datos antiguos.
- ✅ Documentación del sistema y del código en GitHub.

## ⛔ Temas actuales
- ❌ El manejo de excepciones podría ser más robusto.
- ❌ La funcionalidad de búsqueda no incluye más de 1 URL.
- ❌ No se han implementado pruebas unitarias completas para todas las vistas.

## 🔧 Posibles mejoras
- ✅ Implementar paginación en los resultados de búsqueda.
- ✅ Mejorar la gestión de excepciones para una retroalimentación más clara.
- ✅ Optimizar el rendimiento del scraping para búsquedas más rápidas.
- ✅ Agregar pruebas unitarias para todas las vistas y modelos.
- ✅ Permitir exportar los artículos seleccionados a formatos como CSV o Excel.

## 👨‍💻 Tecnologías utilizadas
- **Backend**: Django (Python), Selenium.
- **Base de datos**: MySQL.
- **Interfaz**: HTML, CSS, Bootstrap.
- **Control de versiones**: Git / GitHub.
- **Metodología**: Scrum.
- **Pruebas**: Pruebas unitarias y de integración con el framework de Django.
- **Librerías útiles**: Scrapy, Requests, Selenium.
- **Gestión del proyecto**: GitHub.

## ⚙ Instalación y uso

### 🔽 Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/webscraper-fusion.git
cd webscraper-fusion
```

### 📦 Instalar dependencias
Crear y activar un entorno virtual:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

Instalar dependencias:
```bash
pip install -r requirements.txt
```

### ⚙ Configurar la base de datos
Asegúrate de tener MySQL instalado y configurado. Luego, crea un archivo `.env` con las credenciales de tu base de datos:

```bash
touch .env
```

Contenido del archivo `.env`:
```env
mysql_username = 'tu_usuario'
mysql_password = 'tu_contraseña'
mysql_host = '127.0.0.1'
mysql_port = 3306
bbdd_name = 'webscraper_db'
```

### ↩️ Realizar migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 🚀 Ejecutar el servidor
```bash
python manage.py runserver
```
Accede a la aplicación en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 🚀 Ejecutar el comando de scraping
```bash
python manage.py scrape
```

## 📂 Estructura de la carpeta

```
PROYECTO_3_WEB_SCRAPER
├── logs
├── scraper
│   ├── __pycache__
│   ├── management
│   │   ├── commands
│   │   │   ├── __pycache__
│   │   │   ├── __init__.py
│   │   │   └── scrape.py
│   │   └── __init__.py
│   ├── migrations
│   ├── services
│   │   ├── __pycache__
│   │   └── __init__.py
│   ├── templates
│   │   ├── scraper
│   │   │   ├── login.html
│   │   │   └── logout_confirm.html
│   ├── tests
│   │   ├── __pycache__
│   │   ├── test_admin.py
│   │   ├── test_commands.py
│   │   ├── test_forms.py
│   │   ├── test_models.py
│   │   ├── test_services.py
│   │   ├── test_views.py
│   │   └── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── static
├── venv
├── webscraper_project
│   ├── __pycache__
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── .env
│   ├── .gitignore
│   ├── db.sqlite3
│   ├── manage.py
│   ├── Readme.md
│   ├── requirements.txt
│   ├── run_tests.py
│   └── scraper.log
```

## 🧪 Realización de pruebas
Se realizan pruebas unitarias para `forms`, `views`, `admin`, `models`, `urls`, `scrapy` en `services` y `commands`. Los comandos individuales para ejecutar las pruebas son:

```bash
python manage.py test scraper.tests.test_admin
python manage.py test scraper.tests.test_forms
python manage.py test scraper.tests.test_models
python manage.py test scraper.tests.test_services
python manage.py test scraper.tests.test_views
python manage.py test scraper.tests.test_commands
```

Además, se ha generado un comando para ejecutar todas las pruebas excepto `test_commands` (que requiere interacción con el usuario):

```bash
python run_tests.py
```

Este comando ejecuta:
- `python manage.py test scraper.tests.test_admin`
- `python manage.py test scraper.tests.test_forms`
- `python manage.py test scraper.tests.test_models`
- `python manage.py test scraper.tests.test_services`
- `python manage.py test scraper.tests.test_views`

El comando `python manage.py test scraper.tests.test_commands` debe ejecutarse individualmente debido a que requiere interacción con el usuario.

## 🌟 Estado del proyecto
El proyecto está en desarrollo. Se han implementado las funcionalidades principales, pero aún hay áreas que requieren mejoras y optimización.

Si este proyecto te resulta útil, ¡marca el repositorio con una estrella en GitHub! ⭐
```

### **Cambios realizados:**
1. Se agregó la sección **🧪 Realización de pruebas** con los comandos individuales y el comando run_tests.py.
2. Se incluyó la nota sobre la ejecución individual de `test_commands` debido a la interacción con el usuario.
3. Se configuraron correctamente los enlaces para que funcionen en GitHub.

Este archivo está listo para ser copiado y pegado en Visual Studio Code. 😊
