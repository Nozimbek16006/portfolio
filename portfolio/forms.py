from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ismingiz"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
            "message": forms.Textarea(attrs={"placeholder": "Xabaringiz", "rows": 6}),
        }
