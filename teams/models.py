from django.db import models
import uuid
# Create your models here.

class Team(models.Model):
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50, unique=True)
  points = models.IntegerField()
  position = models.IntegerField()
  wins = models.IntegerField()
  losses = models.IntegerField()
  description = models.TextField()

  def __str__(self):
    return self.name



class Player(models.Model):
  # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField(max_length=50)
  position = models.CharField(max_length=50)
  team = models.ForeignKey(Team, on_delete=models.CASCADE) #if team deleted, delete all players associated with it

  def __str__(self):
    return self.name
  




