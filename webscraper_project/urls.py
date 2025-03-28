"""
URL configuration for webscraper_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# filepath: c:\Users\admin\Desktop\proyectos 3-versionaes\webscraper_fusion_2\webscraper_fusion_2\urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from scraper import views
from scraper.views import CustomLoginView, CustomLogoutView  # Importar las vistas de login y logout

urlpatterns = [
    # Admin URLs
    path('admin/', admin.site.urls),

    # Página de inicio
    path('', views.home, name='home'),

    # URLs del scraper
    path('scraper/', include('scraper.urls')),

    # URLs de login y logout
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
]

# Servir archivos estáticos en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)