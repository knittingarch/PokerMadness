from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


class Game(models.Model):
    GAME_STATE_CHOICES = (
        (PROPOSED, "Proposed"),
        (CONFIRMED, "Confirmed"),
        (CANCELLED, "Cancelled"),
    )
    game_state = models.CharField(
        max_length=255,
        choices=GAME_STATE_CHOICES,
        default=PROPOSED,
    )
    date = models.DateField
    player = models.CharField(max_length=255)


class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)