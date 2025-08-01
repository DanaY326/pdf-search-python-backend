from django import forms
from .models import pdfData

class pdfDataForm(forms.ModelForm):
    class Meta:
        model = pdfData
        fields = "__all__"