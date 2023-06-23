from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ('country', 'first_name', 'last_name', 'address', 'city', 'postal_code', 'email', 'phone',)

    labels = {
        "country": "",
        "first_name": "",
        "last_name": "",
        "address": "",
        "city": "",
        "postal_code": "",
        "email": "",
        "phone": "",
    }

    placeholders = {
        "country": "Enter your country",
        "first_name": "Enter your first name",
        "last_name": "Enter your last name",
        "address": "Enter your address",
        "city": "Enter your city",
        "postal_code": "Enter your postal code",
        "email": "Enter your email",
        "phone": "Enter your phone number",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.label = self.labels.get(field_name, field.label)
            field.widget.attrs['placeholder'] = self.placeholders.get(field_name, '')

