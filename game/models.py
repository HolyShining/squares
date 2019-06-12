from django.db import models


# Create your models here.

class GameHistory(models.Model):
    """Model for storing results of every game at database"""

    class Meta:
        db_table = 'game_history'
        ordering = ['id']

    players = models.IntegerField(null=True)
    squares = models.IntegerField(null=True)
    cards = models.IntegerField(null=True)
    sequence = models.CharField(max_length=79, null=True)
    deck = models.TextField(max_length=600, null=True)
    result = models.CharField(max_length=60, null=True)
