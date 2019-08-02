from django.db import models


class Player(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    api_key = models.IntegerField()
    name = models.CharField(max_length=255)
    cooldown = models.IntegerField(null=True)
    encumbrance = models.IntegerField(null=True)
    strength = models.IntegerField(null=True)
    speed = models.IntegerField(null=True)
    gold = models.IntegerField(null=True)
    inventory = models.TextField(blank=True)
    status = models.TextField(blank=True)
    has_mined = models.BooleanField(null=True)
    errors = models.TextField(blank=True)
    messages = models.TextField(blank=True)
    current_room = models.IntegerField(null=True)

    def __str__(self):
        return f'#{self.username} {self.name}'


class Room(models.Model):
    room_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    coordX = models.IntegerField()
    coordY = models.IntegerField()
    exitN = models.CharField(max_length=255)
    exitE = models.CharField(max_length=255)
    exitS = models.CharField(max_length=255)
    exitW = models.CharField(max_length=255)
    notes = models.TextField(blank=True)
    elevation = models.IntegerField(null=True)
    terrain = models.CharField(max_length=255, blank=True)
    players = models.TextField(blank=True)
    items = models.TextField(blank=True)
    cooldown = models.FloatField(null=True)
    errors = models.TextField(blank=True)
    messages = models.TextField(blank=True)

    def __str__(self):
        return f'#{self.room_id} {self.title}'
