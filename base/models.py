from django.db import models

# Create your models here.

class Room(models.Model):
    # host
    # topic
    name = models.CharField(max_length=200) #
    description = models.TextField(null=True, blank=True) # null is by default set to false - resetting it to true allows the dsc to be left blank
    # participants = 
    updated = models.DateTimeField(auto_now=True) #taking a timestamp for whenever there's an update to the model instance or table
    created = models.DateTimeField(auto_now_add= True) #auto_now takes a snapshot everytime there's an update while auto_now_add takes a snapshot just once 


    def __str__(self):
        return self.name
    