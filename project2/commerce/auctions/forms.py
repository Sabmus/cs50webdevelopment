from django import forms
from . import models


class CreateListingForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'
        exclude = ["owner", "last_until"]
