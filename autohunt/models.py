from django.db import models


class Room(models.Model):
    room_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    coordX = models.IntegerField()
    coordY = models.IntegerField()
    exitN = models.IntegerField()
    exitE = models.IntegerField()
    exitS = models.IntegerField()
    exitW = models.IntegerField()
    notes = models.TextField()
