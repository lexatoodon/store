from django import forms
from review.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        widgets = {
            'text': forms.Textarea(attrs={
                'rows':'2',
                'class':'form-control',
                'placeholder':'What are you thinking?'
            }),
            'rating': forms.NumberInput(attrs={
                'placeholder':'Rate from 1 to 5',
                'max':'5.0',
                'min':'1.0',
                'step':'0.1'
            })
        }