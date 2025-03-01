from django import forms

class HousePriceForm(forms.Form):
    bedrooms = forms.IntegerField(label='Number of Bedrooms', min_value=1)
    bathrooms = forms.IntegerField(label='Number of Bathrooms', min_value=1)
    sqft = forms.IntegerField(label='Size in Square Feet', min_value=100)
    location = forms.IntegerField(label='Location Code (1-5)', min_value=1, max_value=5)
