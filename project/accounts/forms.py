from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : "Username"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : "Password"
    }))

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'first Name'
    }))

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Re-Type Password'
    }))

    class Meta:
        model = User
        fields = ['first_name','last_name', 'username', 'email', 'password1', 'password2']



'''from django import forms
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
        fields = ['firstName', 'lastName', 'email', 'phone', 'message']'''