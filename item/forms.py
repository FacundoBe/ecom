from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','is_sold','created_by','image',)
