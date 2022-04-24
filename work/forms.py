from django import forms
from .models import Cart


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 1000)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=str)