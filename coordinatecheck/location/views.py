from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from .forms import RegionsForm, LocForm
from .models import Regions, Loc
import math
from django.core.urlresolvers import reverse


def index(request):
  if request.method == 'POST':
    form = RegionsForm(request.POST)
    # Saving the values to the db
    if form.is_valid():
      obj = Regions()  # object of the table in db
      # passing values from the form to the db
      obj.place = form.cleaned_data['place']
      obj.lat = form.cleaned_data['lat']
      obj.lng = form.cleaned_data['lng']
      obj.formatted_address = form.cleaned_data['formatted_address']
      obj.country_short = form.cleaned_data['country_short']
      obj.score = form.cleaned_data['score']
      # persisting the db value
      obj.save()
      return HttpResponseRedirect('/location/')
  else:
    form = RegionsForm()
  return render(request, 'location/index.html', {'form': form})


def enterloc(request):
  form = LocForm(request.POST)
  # Saving the values to the db
  if form.is_valid():
    obj = Loc()  # object of the Loc table in db
    # passing values from the form to the db
    obj.place = form.cleaned_data['place']
    obj.lat = form.cleaned_data['lat']
    obj.lng = form.cleaned_data['lng']
    obj.formatted_address = form.cleaned_data['formatted_address']
    obj.country_short = form.cleaned_data['country_short']
    obj.score = 0  # intial value of score is 0
    # This will be updated soon

    # To seperate the city,state adn country
    string = obj.place.split(',')
    # The last element will be country
    con = string[-1]
    state = ""
    if len(string) > 1:
      # The second last element will be state if the list contains more than one element
      state = string[-2]
    # calculating the score

    # fetch all the values in db
    # This can consume time but as our db size is small it is efficient enough else have to query
    data = Regions.objects.all()
    result = []
    # score_putback is the variable calculating the cumulative score
    score_putback = 0
    # count calculates the number of times if location is inside a region already in the regions table
    count = 0
    # Iterate through all the entries in the db to find the distance
    for reg in data:
      # To seperate the city,state and country
      # strip is used to remove the white spaces
      string1 = reg.place.split(',')
      if ((con.strip() == string1[0].strip())):
        score_putback = score_putback + reg.score
        count += 1
      if (state.strip() == string1[0].strip()):
        score_putback = score_putback + reg.score
        count += 1
      # Use Law of Cosines to find nearest point
      # It is most efficient method to use for lat lng comparisons according to the internet
      lat1 = reg.lat
      lat2 = obj.lat
      lng1 = reg.lng
      lng2 = obj.lng
      if lat1 == lat2 and lng1 == lng2:
        distance = 0
        score1 = [distance, reg.score, score_putback]
        result.append(score1)
      else:
        delta = lng2 - lng1
        a = math.radians(lat1)
        b = math.radians(lat2)
        C = math.radians(delta)
        x = math.sin(a) * math.sin(b) + math.cos(a) * math.cos(b) * math.cos(C)
        distance = math.acos(x)  # in radians
        distance = math.degrees(distance)  # in degrees
        distance = distance * 60  # 60 nautical miles / lat degree
        distance = distance * 1852  # conversion to meters
        # the distance in meters from the law of cosines
        distance = round(distance)
        # making a list containing the distance, its corresponding score and cumulative score
        score1 = [distance, reg.score, score_putback]
        result.append(score1)
    # sorting the list in ascending order of distance
    result.sort(key=lambda x: x[0])
    # persisting the db value

    # When the country and state is not database count will be 0 and location is also not in db
    # Then score should be 0
    if count == 0 and result[0][0] != 0:
      score_putback = 0
    # When the country or state is already present in the database the count will be >0
    # If the minimum distance is 0 that means the test location is already in the db
    # score_putback would contain the country or state's value.
    elif count > 0 and result[0][0] == 0:
      score_putback += result[0][1]
    # All other cases
    else:
      # In this case score_putback would be 0 before this line and therefore
      score_putback += result[0][1]
    form.cleaned_data['score'] = score_putback
    obj.score = score_putback
    obj.save()
    # To populate the cumulative score
    score = {'score': obj.score}
    return render(request, 'location/check/enterloc.html', {'score': score})
  else:
    form = LocForm()
  return render(request, 'location/check/enterloc.html')
