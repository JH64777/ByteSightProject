from django import forms

class SteganographyForm(forms.Form):
    coverimg = forms.ImageField(label='Cover Image', required=True)
    secretdata = forms.FileField(label='Secret Data', required=True)