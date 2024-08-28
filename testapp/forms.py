from django import forms
from . models import Users
class UserRegistration(forms.ModelForm):
    class Meta:
        model=Users
        fields=('Username','Password','Confirm_password')