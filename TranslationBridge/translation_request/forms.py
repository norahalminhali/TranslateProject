from django import forms
from .models import TranslationRequest



class TranslationRequestForm(forms.ModelForm):
    class Meta:
        model = TranslationRequest
        fields = '__all__'

        widgets = {
            "company_name": forms.TextInput(attrs={
                "class": "form-control mt-2",
                "placeholder": "Enter Company Name..."
            }),
            "company_type": forms.Select(attrs={
                "class": "form-control"
            }),
            "request_type": forms.HiddenInput(),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3
            }),
        }



