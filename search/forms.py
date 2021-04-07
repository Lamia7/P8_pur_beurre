"""Creates forms for 'search' app"""

from django import forms


class MainSearchForm(forms.Form):
    """Represents the main search form on the home page"""
    product_search = forms.CharField(
        label="",
        max_length=70,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Entrez un produit",
                "class": "form-control",
                "type": "text",
                "autofocus": "autofocus",
            }
        ),
    )


class NavSearchForm(forms.Form):
    """Represents the search form on the navigation bar"""
    product_search = forms.CharField(
        label="",
        max_length=70,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Entrez un produit",
                "class": "form-control",
                "type": "text",
            }
        ),
    )
