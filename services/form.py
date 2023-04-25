from django import forms
from .models import Contact


class ContactForm(forms.Form):
    
    nom = forms.CharField(label='', widget=forms.TextInput(
         attrs={
            'placeholder':'Nom et prénom(s):',
            'class': 'nom'
        }
    ))

    telephone = forms.IntegerField(label='', widget=forms.NumberInput(
        attrs={
            'placeholder':'Numéro de téléphone:',
            'class': 'telephone'
        }
    ))

    email = forms.EmailField(label='',required=False, widget=forms.EmailInput(
        attrs={
            'placeholder':'Adresse email (***optionnel):',
            'class':'email',
        }
    ))
    
    code_produit = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'placeholder':'Code du produit',
            'class': 'code_produit',
        }
    ))

    message = forms.CharField(label='', required=False, widget=forms.Textarea(
        attrs={
            'placeholder':'Un message particulier pour nous ? (***optionnel) ',
            'class': 'message',
        }
    ))
  

