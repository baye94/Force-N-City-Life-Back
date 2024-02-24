from django import forms

from .models import Produit

class ProduitForms(forms.ModelForm):
    class Meta:
        model=Produit
        fields=('name','content','prix')
