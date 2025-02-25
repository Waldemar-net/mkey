from django import forms
 
from .models import Gallery, Products
 
 
class CommentForm(forms.Form):
    parent_comment = forms.IntegerField(
        widget=forms.HiddenInput,
        required=False
    )
 
    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )

class AddProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            'name',
            'slug',
            'description',
            'image',
            'poster',
            'is_displayed',
            'price',
            'discount',
            'category',
            'genry',
            'platform',
            'system',
            'rampc',
            'direx',
            'disk',
            'languages',
            'region',
            'services',
            'additional',
            'publisher',
            'developer',
            'video',
            'datas',
            'processor',
            'videocard',
            
        ]
        
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'slug' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
            'image' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'poster' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_displayed' : forms.CheckboxInput(attrs={'class': 'form-control'}),
            'price' : forms.TextInput(attrs={'class': 'form-control'}),
            'discount' : forms.TextInput(attrs={'class': 'form-control'}),
            'category' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'genry' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'platform' : forms.Select(attrs={'class': 'form-control'}),
            'system' : forms.Select(attrs={'class': 'form-control'}),
            'rampc' : forms.Select(attrs={'class': 'form-control'}),
            'direx' : forms.Select(attrs={'class': 'form-control'}),
            'disk' : forms.Select(attrs={'class': 'form-control'}),
            'languages' : forms.Select(attrs={'class': 'form-control'}),
            'region' : forms.Select(attrs={'class': 'form-control'}),
            'services' : forms.Select(attrs={'class': 'form-control'}),
            'additional' : forms.TextInput(attrs={'class': 'form-control'}),
            'publisher' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'developer' : forms.SelectMultiple(attrs={'class': 'form-control'}),
            'video' : forms.TextInput(attrs={'class': 'form-control'}),
            'datas' : forms.DateInput(attrs={'class': 'form-control'}),
            'processor' : forms.TextInput(attrs={'class': 'form-control'}),
            'videocard' : forms.TextInput(attrs={'class': 'form-control'}),
            


        }

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['image']