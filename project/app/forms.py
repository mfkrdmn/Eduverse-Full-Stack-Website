from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    firstName = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "First Name"
    }))
    lastName = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Last Name"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder' : 'Email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Phone Number'
    }))
    message = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your message'
    }))

    class Meta:
        model = Contact
        fields = ['firstName', 'lastName', 'email', 'phone', 'message']