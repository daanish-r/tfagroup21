from django.forms import ModelForm
from .models import Fields

class SightingForm(ModelForm):
    class Meta:
        model = Fields
        fields = '__all__'
