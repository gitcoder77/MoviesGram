from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'actor', 'language', 'category', 'release_date', 'img', 'youtube', 'desc']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),
        }