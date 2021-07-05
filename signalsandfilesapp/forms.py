from django import forms
from django.core.validators import validate_email, MinLengthValidator, MaxLengthValidator


class UserForm(forms.Form):
    firstName = forms.CharField(widget=forms.TextInput({
        'placeholder': 'Enter FirstName', 'name': 'firstName'
    }))
    lastName = forms.CharField(widget=forms.TextInput({
        'placeholder': 'Enter LastName', 'name': 'lastName'
    }))
    username = forms.CharField(widget=forms.TextInput({
        'placeholder': 'Enter UserName', 'name': 'username'
    }),validators=[MinLengthValidator(5),MaxLengthValidator(20)])
    password = forms.CharField(widget=forms.PasswordInput({
        'placeholder': 'Enter Password', 'name': 'password'
    }))
    email = forms.EmailField(widget=forms.EmailInput({
        'placeholder': 'Enter Email', 'name': 'email'
    }),validators=[validate_email])
    image = forms.ImageField(
        widget=forms.ClearableFileInput({'placeholder': 'Upload ProfilePicture', 'name': 'image'}))
    file = forms.FileField(widget=forms.ClearableFileInput(
        {'placeholder': 'Upload File', 'id': 'file', 'class': 'fileUpload', 'name': 'file','multiple':True}))
