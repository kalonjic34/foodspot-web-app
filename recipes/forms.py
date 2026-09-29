from django import forms

class SearchForm(forms.Form):
    forms.CharField(label='',widget=forms.TextInput(
        attrs={
            'placeholder':'Search recipes...',
            'class':'form-control mr-sm-2'
            
        }
    ))
    
