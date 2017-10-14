from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import models
from datetime import date  
import django.utils.timezone
from django.contrib import auth

class LogGame(models.Model):
	game_date = models.DateField(blank=True,)
	yourScore = models.IntegerField()
	opponentScore = models.IntegerField()
	opponent = models.OneToOneField(settings.AUTH_USER_MODEL)

	def __str__(self):
		return self.opponent