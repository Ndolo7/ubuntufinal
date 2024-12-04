from django import forms
from .models import Fundraiser


class FundraisersBasicDetailsForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['title', 'description', 'goal_amount', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }



