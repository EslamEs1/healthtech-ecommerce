from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ('country', 'first_name', 'last_name', 'address', 'city', 'postal_code', 'email', 'phone',)
