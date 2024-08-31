from django import forms
from .models import SteganalysisIMG

class StegoForm(forms.ModelForm): # 이것에 대해 알아볼 것
    class Meta:
        model = SteganalysisIMG
        fields = ['imgfile']
        labels = {
            'imgfile' : '이미지'
        }