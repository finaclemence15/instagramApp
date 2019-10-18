from django import forms
from .models import Image

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['poster']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }