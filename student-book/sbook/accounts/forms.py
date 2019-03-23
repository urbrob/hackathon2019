from django import forms

class RegistrationForm(forms.Form):
	email=forms.CharField(widget=forms.TextInput(attrs={'type':'email', 'class':'form-control'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
