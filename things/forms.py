"""Forms of the project."""
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your forms here.

class Form(forms.Form):
    name = forms.CharField(label="Name",max_length=35)
    description = forms.Textarea(label="Description",max_length=120)
    quantity = forms.CharField(label="Name",
                               validators=[MinValueValidator(0),MaxValueValidator(50)], 
                               widget=forms.NumberInput())
