from __future__ import unicode_literals

from datetime import datetime, date, time, timedelta
import calendar
import datetime
from django.conf import settings
from django.db import models
import django.utils.timezone
from django.contrib import auth

CHOICES = (
        ('SMALL', '2'),
        ('MEDIUM', '4'),
        ('LONG', '8'),
        )

fecha2 = date.today() + timedelta(days=2)


class LogService(models.Model):
	#hours = models.CharField(max_length=20, choices=CHOICES, blank=True, null=True)
	hours = models.CharField(max_length=255, choices=CHOICES, default="8")
	date_delivery = models.DateField(default=fecha2, blank=True)
	time_entry = models.TimeField(['%I:%H %p'], blank=True, null=True)
	direction = models.CharField(max_length=5000, blank=True, null=True)

	def __str__(self):
		return self.hours