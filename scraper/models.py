from django.db import models



from django.db import models

class SelectedArticle(models.Model):
    title = models.CharField(max_length=500)
    authors = models.TextField()  # Cambiado de CharField a TextField
    citation = models.TextField()
    journal = models.CharField(max_length=500)
    source_url = models.URLField(unique=True)  # Evitar duplicados por URL
    publication_date = models.DateField(null=True, blank=True)  # Permitir valores nulos
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class DuplicateArticle(models.Model):
    title = models.CharField(max_length=500)
    authors = models.TextField()  # Cambiado de CharField a TextField
    citation = models.TextField()
    journal = models.CharField(max_length=500)
    source_url = models.URLField(unique=True)  # Evitar duplicados por URL
    publication_date = models.DateField(null=True, blank=True)  # Permitir valores nulos
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title