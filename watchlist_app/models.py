import datetime
from django.db import models

class StreamPlatform(models.Model):
    
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
    

# Create your models here.
class WatchList(models.Model):
   
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name="watchlist")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) :
        return self.title
    
class BusinessType(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default="UNKNOWN")
    detail = models.CharField(max_length=200, default="UNKNOWN")
    
    def __str__(self):
        return self.name

class BusinessPlace(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_user = models.CharField(max_length=200, default="UNKNOWN")
    name = models.CharField(max_length=200, default="UNKNOWN")
    detail = models.CharField(max_length=200, default="UNKNOWN")
    price = models.FloatField(default=0)
    lat = models.CharField(max_length=25, default="UNKNOWN")
    lng = models.CharField(max_length=25, default="UNKNOWN")
    district = models.CharField(max_length=200, default="UNKNOWN")
    province = models.CharField(max_length=200, default="UNKNOWN")
    timeOpen = models.TimeField(blank=True, null=True)
    timeClose = models.TimeField(blank=True, null=True)
    website = models.CharField(max_length=200, default="UNKNOWN")
    type = models.name = models.ForeignKey(BusinessType, related_name='business_type', on_delete=models.CASCADE)
    pinPhotograph = models.TextField(blank=True, null=True)
    pinCheckIn = models.TextField(blank=True, null=True)
    recomendStatus = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

class Trip(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_user = models.CharField(max_length=200, default="UNKNOWN")
    detail = models.CharField(max_length=200, default="UNKNOWN")
    title = models.CharField(max_length=200, default="UNKNOWN")
    position_start = models.CharField(max_length=200, default="UNKNOWN")
    position_end = models.CharField(max_length=200, default="UNKNOWN")
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    budget = models.FloatField(default=0)
    total_cost = models.FloatField(default=0)
    places = models.TextField(default="UNKNOWN")
    permission = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
class BusinessPlacePicture(models.Model):
    
    id = models.AutoField(primary_key=True)
    id_place = models.ForeignKey(BusinessPlace, related_name="business_place", on_delete=models.CASCADE)
    link = models.TextField()
    
    def __str__(self):
        return self.link