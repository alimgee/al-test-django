from django import forms
from .models import Item


class ItemForm(forms.ModelForm):

    class Meta:
        # create item form with 2 fields, called from models.py
        model = Item
        fields = ('name', 'done')