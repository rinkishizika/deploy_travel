from django import forms
from .models import Restaurant
from .models import PlaceStay
from .models import Activities


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['restaurant_id', 'restaurant_name', 'restaurant_desc', 'restaurant_signature', 'restaurant_rating']

class PlaceStayForm(forms.ModelForm):
    class Meta:
        model = PlaceStay
        fields = ['place_id', 'place_name', 'place_type', 'place_desc', 'place_rating']

class ActivitiesForm(forms.ModelForm):
    class Meta:
        model = Activities
        fields = ['activities_id', 'activities_name', 'activities_desc', 'activities_price', 'activities_rating']