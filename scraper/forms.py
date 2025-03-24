from django import forms
from .models import SelectedArticle, DuplicateArticle

class SelectedArticleForm(forms.ModelForm):
    class Meta:
        model = SelectedArticle
        fields = '__all__'

class DuplicateArticleForm(forms.ModelForm):
    class Meta:
        model = DuplicateArticle
        fields = '__all__'