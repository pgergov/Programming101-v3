from django import forms

class UserPassForm(forms.Form):
    username = forms.CharField(label="Your username")
    passw = forms.CharField(label="Your password")
