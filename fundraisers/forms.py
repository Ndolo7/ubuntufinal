from django import forms
from .models import Fundraiser


class FundraisersBasicDetailsForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['title', 'description', 'goal_amount', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    

class FundraisersPersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['full_name', 'email', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.TextInput(attrs={'placeholder': 'johndoe@example.com'}),
            'phone_number': forms.NumberInput(attrs={'min': 10}),
        }
        