from django import forms
from . import models


class CreateListingForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields = '__all__'
        exclude = ["owner", "slug", "last_until"]


class CreateBidForm(forms.ModelForm):
    class Meta:
        model = models.Bid
        fields = ["amount", "currency"]
