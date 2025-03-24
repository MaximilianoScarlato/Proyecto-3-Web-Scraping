from django.contrib import admin
from .models import SelectedArticle, DuplicateArticle

@admin.register(SelectedArticle)
class SelectedArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'journal', 'publication_date', 'created_at')
    search_fields = ('title', 'authors', 'journal')

@admin.register(DuplicateArticle)
class DuplicateArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'journal', 'publication_date', 'created_at')
    search_fields = ('title', 'authors', 'journal')