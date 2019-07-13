from django import forms
from application.models import *

class r_productBuyForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['tQty']
