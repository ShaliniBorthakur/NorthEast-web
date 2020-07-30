from .models import Product
from django import forms
from django.forms import ModelForm


class ProductCreateForm(forms.ModelForm):
    # quantity_ever_stocked = forms.CharField(label="Quantity Ever Stocked", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Quantity Ever Stocked', 'rows': '1', 'cols': '30'}))
    class Meta:
        model = Product
        fields = ('product_name','category', 'subcategory', 
                    'price', 'desc', 'quantity', 'image')


class ProductEditForm(forms.ModelForm):
    image = forms.FileField(required = False)
    class Meta:
        model = Product
        fields = ('product_name','category', 'subcategory', 
                    'price', 'desc', 'image')
