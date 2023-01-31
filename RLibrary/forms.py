from django import forms

class SignUpForm(forms.Form):
    firstName = forms.CharField(max_length=50, label="First Name")
    lastName = forms.CharField(max_length=50, label="Last Name")
    UserName = forms.CharField(max_length=50, label= "Choose a Username")
    Email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(min_length=8, label="Create a Password", widget=forms.PasswordInput)
    password2 = forms.CharField(min_length=8, label="Confirm Password", widget=forms.PasswordInput)
    