from django import forms
from translators.models import Translator

#Create the form class
class TranslatorForm(forms.ModelForm):
    class Meta:
        model = Translator
        fields = ["specialty", "experience", "city", "languages"]
