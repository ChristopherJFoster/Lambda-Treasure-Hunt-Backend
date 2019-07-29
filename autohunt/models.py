from django.db import models


class Room(models.Model):
    room_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    coordX = models.IntegerField()
    coordY = models.IntegerField()
    exitN = models.CharField(max_length=1, blank=True)
    exitE = models.CharField(max_length=1, blank=True)
    exitS = models.CharField(max_length=1, blank=True)
    exitW = models.CharField(max_length=1, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'#{self.room_id} {self.title}'
