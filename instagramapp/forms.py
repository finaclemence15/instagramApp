from django import forms
from .models import Image, Profile, Comments

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments', 'profile','username']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }
        
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = []        
       