from django import forms
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    # TRUE_FALSE_CHOICES = (
    #     (True, 'Wholesaler'),
    #     (True, 'Retailer'))
    # boolfield = forms.ChoiceField(choices = TRUE_FALSE_CHOICES, label="Select Type", widget=forms.Select(), required=True)

    # is_whole = forms.BooleanField(widget=forms.CheckboxInput, required = False)
    # is_retail = forms.BooleanField(widget=forms.CheckboxInput, required = False)
    class Meta:
        model = Profile
        fields = ['image']
