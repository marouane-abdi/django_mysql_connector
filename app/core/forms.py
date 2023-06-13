from django import forms
from .models import Person

class SubmitForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'age', 'phoneNumber', 'city', 'country', 'occupation']
