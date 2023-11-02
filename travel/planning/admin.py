from django.contrib import admin
from .models import SignUp, Activities, Restaurant, PlaceStay, Location

# Register your models here.
admin.site.register(SignUp)
admin.site.register(Activities)
admin.site.register(Restaurant)
admin.site.register(PlaceStay)
admin.site.register(Location)

