from django import forms
from .models import Bird

class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ['name', 'feather_color', 'image']