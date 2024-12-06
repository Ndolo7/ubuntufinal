from django import forms
from .models import Fundraiser


class FundraisersBasicDetailsForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['title', 'description', 'goal_amount', 'category']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    def is_valid(self):
        # Use self.data instead of self.get()
        if self.data.get('goal_amount'):
            # Convert Decimal to float for session storage
            self.data['goal_amount'] = float(self.data['goal_amount'])
        return super().is_valid()


class FundraisersPersonalDetailsForm(forms.ModelForm):
    class Meta:
        model = Fundraiser
        fields = ['full_name', 'email', 'phone_number']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
            'email': forms.TextInput(attrs={'placeholder': 'johndoe@example.com'}),
            'phone_number': forms.NumberInput(attrs={'min': 10}),
        }
        def is_valid(self):
        # Use self.data instead of self.get()
             if self.data.get('goal_amount'):
            # Convert Decimal to float for session storage
                 self.data['goal_amount'] = float(self.data['goal_amount'])
             return super().is_valid()
