from django.forms import ModelForm
from .models import Conversion

class CurrencyForm(ModelForm):
    class Meta:
        model = Conversion
        fields = ['from_currency', 'value', 'to_currency']
