from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200) #
    description = models.TextField(null=True, blank=True) # null is by default set to false - resetting it to true allows the dsc to be left blank
    # participants = 
    updated = models.DateTimeField(auto_now=True) #taking a timestamp for whenever there's an update to the model instance or table
    created = models.DateTimeField(auto_now_add= True) #auto_now takes a snapshot everytime there's an update while auto_now_add takes a snapshot just once 


    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #on_delete is a required argument for foreign key relationships. CASCADE means if the user is deleted, all messages will be deleted as well
    room = models.ForeignKey(Room, on_delete=models.CASCADE) #on_delete is a required argument for foreign key relationships. CASCADE means if the room is deleted, all messages will be deleted as well
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) #taking a timestamp for whenever there's an update to the model instance or table
    created = models.DateTimeField(auto_now_add= True) #auto_now takes a snapshot

    def __str__(self):
        return self.body[0:50] #returning the first 50 characters of the message body
    

