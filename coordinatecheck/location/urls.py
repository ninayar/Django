"URL section"

from django.conf.urls import url
from . import views

app_name = 'location'

urlpatterns = [
  # my index page
  # Regions page
  url(r'^$', views.index, name='index'),
  # location page
  url(r'^check/$', views.enterloc, name='enterloc'),
]
