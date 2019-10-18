from django import forms
from .models import Image, Profile

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['poster', 'profile','likes']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []        
       