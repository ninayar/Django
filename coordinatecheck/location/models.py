from django.db import models


# Create your models here.
# Region Table with the associated score
class Regions(models.Model):
  place = models.CharField(max_length=150, default="NONE")
  lat = models.FloatField(default=0.0)
  lng = models.FloatField(default=0.0)
  formatted_address = models.CharField(max_length=150, default="NONE")
  country_short = models.CharField(max_length=10, default="NONE")
  score = models.IntegerField(default=0, primary_key=True)


# Location Table for storing the test data
class Loc(models.Model):
  place = models.CharField(max_length=150, default="NONE")
  lat = models.FloatField(default=0.0)
  lng = models.FloatField(default=0.0)
  formatted_address = models.CharField(max_length=150, default="NONE")
  country_short = models.CharField(max_length=10, default="NONE")
  score = models.IntegerField(default=0)
