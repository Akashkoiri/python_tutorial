from django import forms

class ListForm(forms.Form):
    name = forms.CharField(max_length=100)
    check = forms.BooleanField()
