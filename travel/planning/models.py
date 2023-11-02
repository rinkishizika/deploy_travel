from django.db import models

# Create your models here.

class SignUp (models.Model):
    email = models.CharField(max_length=40, primary_key=True)
    phoneNo = models.CharField(max_length=14)
    nickname = models.TextField()
    password = models.CharField(max_length=30)

class Activities (models.Model):
    activities_id = models.CharField(max_length=5, primary_key=True)
    activities_name = models.TextField()
    activities_desc = models.TextField()
    activities_price = models.FloatField()
    activities_rating = models.IntegerField()

class Restaurant (models.Model):
    restaurant_id = models.CharField(max_length=5, primary_key=True)
    restaurant_name = models.TextField()
    restaurant_desc = models.TextField()
    restaurant_signature = models.TextField()
    restaurant_rating = models.IntegerField()

class PlaceStay (models.Model):
    place_id = models.CharField(max_length=5, primary_key=True)
    place_name = models.TextField()
    place_type = models.TextField()
    place_desc = models.TextField()
    place_rating = models.IntegerField()

class Location (models.Model):
    loc_id = models.CharField(max_length=5, primary_key=True)
    location_name = models.TextField()
    location_desc = models.TextField()
    email = models.ForeignKey(SignUp,on_delete=models.CASCADE)
    activities_id = models.ForeignKey(Activities,on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    place_id = models.ForeignKey(PlaceStay,on_delete=models.CASCADE)





    
    
    
