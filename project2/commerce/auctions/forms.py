from django import forms
from . import models


class CreateListingForm(forms.ModelForm):
    class Meta:
        model = models.Auction
        fields = '__all__'
        exclude = ["user"]
