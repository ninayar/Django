from django import forms
from .models import Regions


class LocationForm(forms.Form):
  place = forms.CharField(max_length=150)


# Region Form with the associated score
class RegionsForm(forms.Form):
  place = forms.CharField()
  lat = forms.FloatField()
  lng = forms.FloatField()
  formatted_address = forms.CharField()
  country_short = forms.CharField()
  score = forms.IntegerField()


# Location form for entering the test data
class LocForm(forms.Form):
  place = forms.CharField()
  lat = forms.FloatField()
  lng = forms.FloatField()
  formatted_address = forms.CharField()
  country_short = forms.CharField()
  score = forms.IntegerField()
