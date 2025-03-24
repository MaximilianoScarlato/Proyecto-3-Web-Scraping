from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import SelectedArticle, DuplicateArticle
from .forms import SelectedArticleForm, DuplicateArticleForm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import urllib.parse
from datetime import datetime
import re
from django.db import IntegrityError
import logging

# Configurar el logger
logger = logging.getLogger(__name__)

# Vista para la página de inicio
@login_required
def home(request):
    return render(request, 'scraper/home.html')

# SelectedArticle Views
@login_required
def selected_article_list(request):
    articles = SelectedArticle.objects.all()
    # Enumerar los artículos
    for index, article in enumerate(articles, start=1):
        article.enumeration = index
    return render(request, 'scraper/selectedarticle_list.html', {'articles': articles})

@login_required
def selected_article_create(request):
    if request.method == 'POST':
        form = SelectedArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('selected_article_list'))
    else:
        form = SelectedArticleForm()
    return render(request, 'scraper/selectedarticle_form.html', {'form': form})

@login_required
def selected_article_update(request, pk):
    article = get_object_or_404(SelectedArticle, pk=pk)
    if request.method == 'POST':
        form = SelectedArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect(reverse('selected_article_list'))
    else:
        form = SelectedArticleForm(instance=article)
    return render(request, 'scraper/selectedarticle_form.html', {'form': form})

@login_required
def selected_article_delete(request, pk):
    article = get_object_or_404(SelectedArticle, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect(reverse('selected_article_list'))
    return render(request, 'scraper/selectedarticle_confirm_delete.html', {'article': article})

# DuplicateArticle Views
@login_required
def duplicate_article_list(request):
    articles = DuplicateArticle.objects.all()
    # Enumerar los artículos
    for index, article in enumerate(articles, start=1):
        article.enumeration = index
    return render(request, 'scraper/duplicatearticle_list.html', {'articles': articles})

# Search Articles
@login_required
def search_articles(request):
    query = request.GET.get('query', '')
    limit = int(request.GET.get('limit', 10))
    articles = []

    if query:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument("user-agent=Mozilla/5.0")
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)

        try:
            encoded_query = urllib.parse.quote(query, safe='')
            base_url = f"https://pubmed.ncbi.nlm.nih.gov/?term={encoded_query}&filter=datesearch.y_1&page="
            total_articles = 0
            page = 1

            while total_articles < limit:
                driver.get(base_url + str(page))
                try:
                    WebDriverWait(driver, 30).until(  # Incrementar el tiempo de espera a 30 segundos
                        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "article.full-docsum"))
                    )
                except TimeoutException:
                    logger.error("TimeoutException: No se encontraron elementos en la página.")
                    break

                articles_on_page = driver.find_elements(By.CSS_SELECTOR, "article.full-docsum")

                for article in articles_on_page:
                    if total_articles >= limit:
                        break
                    try:
                        title = article.find_element(By.CSS_SELECTOR, "a.docsum-title").text.strip()
                        authors = article.find_element(By.CSS_SELECTOR, "span.docsum-authors").text.strip()
                        citation = article.find_element(By.CSS_SELECTOR, "span.docsum-journal-citation").text.strip()
                        source_url = article.find_element(By.CSS_SELECTOR, "a.docsum-title").get_attribute("href")
                        match = re.search(r"(\d{4} \w{3} \d{1,2})", citation)
                        publication_date = datetime.strptime(match.group(1), "%Y %b %d").date() if match else None

                        # Convertir la fecha a cadena para que sea serializable en JSON
                        articles.append({
                            'id': len(articles) + 1,  # Enumerar los artículos
                            'title': title,
                            'authors': authors,
                            'citation': citation,
                            'journal': "PubMed",
                            'source_url': source_url,
                            'publication_date': publication_date.strftime('%Y-%m-%d') if publication_date else None,
                        })
                        total_articles += 1
                    except Exception as e:
                        logger.error(f"Error al procesar un artículo: {e}")
                page += 1
        finally:
            driver.quit()

    # Guardar los artículos en la sesión
    request.session['articles'] = articles

    return render(request, 'scraper/search.html', {'articles': articles})

# Save Articles
@login_required
def save_articles(request):
    if request.method == 'POST':
        selected_ids = request.POST.getlist('selected_articles')
        articles = request.session.get('articles', [])

        for article_id in selected_ids:
            article = next((a for a in articles if str(a['id']) == article_id), None)
            if article:
                # Convertir la fecha de publicación de cadena a objeto date
                publication_date = datetime.strptime(article['publication_date'], '%Y-%m-%d').date() if article['publication_date'] else None

                try:
                    # Intentar guardar el artículo en SelectedArticle
                    SelectedArticle.objects.create(
                        title=article['title'],
                        authors=article['authors'],
                        citation=article['citation'],
                        journal=article['journal'],
                        source_url=article['source_url'],
                        publication_date=publication_date
                    )
                except IntegrityError:
                    # Si el artículo ya existe, guardarlo en DuplicateArticle
                    DuplicateArticle.objects.get_or_create(
                        title=article['title'],
                        authors=article['authors'],
                        citation=article['citation'],
                        journal=article['journal'],
                        source_url=article['source_url'],
                        publication_date=publication_date
                    )

        return redirect('selected_article_list')

# Vistas de Login y Logout
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    template_name = 'logout_confirm.html'