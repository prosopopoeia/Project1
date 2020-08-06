from django import forms

class AddPageForm(forms.Form):
    title = forms.CharField(label='Title', max_length=40)
    body = forms.CharField(label='body', max_length=100)