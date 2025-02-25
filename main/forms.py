from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    problem = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    order_number = forms.CharField(max_length=50)