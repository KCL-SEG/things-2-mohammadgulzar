"""Forms of the project."""
from django import forms

from .models import User

# Create your forms here.

class Form(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'description', "quantity"]
        widgets = { "description": forms.Textarea(), "quantity": forms.NumberInput()}