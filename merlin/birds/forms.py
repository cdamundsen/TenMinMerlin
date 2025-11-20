from django import forms
from .models import Order, Family, Genus, Location, Species


class NewOrderForm(forms.ModelForm):
    class Meta: 
        model = Order
        fields = ['name',]
    

class NewFamilyForm(forms.ModelForm):
    class Meta:
        model = Family
        fields = ['name']


class NewGenusForm(forms.ModelForm):
    class Meta:
        model = Genus
        fields = ['name',]


class NewSpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ['common_name', 'species', 'link',]


class NewLocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields  = ['name', 'description',]