from django import forms
from .models import Contact

from django import forms



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone_number', 'another_phone', 'description']