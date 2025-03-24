from django.urls import path
from . import views

urlpatterns = [
    # SelectedArticle URLs
    path('selected/', views.selected_article_list, name='selected_article_list'),
    path('selected/create/', views.selected_article_create, name='selected_article_create'),
    path('selected/update/<int:pk>/', views.selected_article_update, name='selected_article_update'),
    path('selected/delete/<int:pk>/', views.selected_article_delete, name='selected_article_delete'),

    # DuplicateArticle URLs
    path('duplicate/', views.duplicate_article_list, name='duplicate_article_list'),

    # Search and Save URLs
    path('search/', views.search_articles, name='search_articles'),  # URL para buscar artículos
    path('save/', views.save_articles, name='save_articles'),
]