from django import forms

from .models import Category, News


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        labels = {
            'name': 'Category Name',
            'slug': 'Category Slug',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category']
        labels = {
            'title': 'News Title',
            'content': 'News Content',
            'category': 'Category',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
