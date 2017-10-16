from __future__ import unicode_literals

from datetime import datetime, date, time, timedelta
import calendar
import datetime
from django.conf import settings
from django.db import models
import django.utils.timezone
from django.contrib import auth
from django.core.urlresolvers import reverse

CHOICES = (
        ('2', 'Dos Horas'),
        ('3', 'Tres Horas'),
        ('8', 'Ocho Horas'),
        )

fecha2 = date.today() + timedelta(days=2)

class Service(models.Model):
	hours = models.CharField(max_length=255, choices=CHOICES ,default='2')
	date_delivery = models.DateField(default=fecha2)
	time_entry = models.TimeField('Hora')
	direction = models.CharField(max_length=5000)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


	def __str__(self):
	 	return str(self.date_delivery)

	def get_absolute_url(self):
		view_name = 'detail'
		return reverse(view_name,kwargs={'pk':self.id})

