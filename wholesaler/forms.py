from django import forms
from application.models import *
from users.models import *


class w_AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['catId','subCatId','pName']


class w_ProductListForm(forms.ModelForm):
    class Meta:
        model = ProductListings
        fields = ['b_price','s_price','qty','pimg','pdDescription']

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'
