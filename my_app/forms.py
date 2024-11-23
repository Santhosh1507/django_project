from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'price', 'description', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full rounded-md p-2 border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'placeholder': 'Enter item name'}),
            'price': forms.NumberInput(attrs={'class': 'form-input mt-1 block w-full rounded-md p-2 border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'placeholder': 'Enter item price'}),
            'description': forms.Textarea(attrs={'class': 'form-input mt-1 block w-full rounded-md p-2 border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'placeholder': 'Enter item description', 'rows': 4}),
            'image_url': forms.URLInput(attrs={'class': 'form-input mt-1 block w-full rounded-md p-2 border-2 border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50', 'placeholder': 'Enter image URL'}),
        }