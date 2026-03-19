from django import forms
from .models import ContactSubmission

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name','email','phone','message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'input','placeholder':'Your full name'}),
            'email': forms.EmailInput(attrs={'class':'input','placeholder':'you@company.com'}),
            'phone': forms.TextInput(attrs={'class':'input','placeholder':'Optional'}),
            'message': forms.Textarea(attrs={'class':'input','placeholder':'Sales training, hiring, bootcamp, placement…','rows':4}),
        }
