from __future__ import unicode_literals
from datetime import datetime, date, time, timedelta
import calendar
from django.conf import settings
from django.db import models
from django.contrib import auth
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import datetime
from django.utils.timezone import utc




CHOICES = (
        ('2', 'Dos Horas'),
        ('3', 'Tres Horas'),
        ('8', 'Ocho Horas'),
        )

#fecha2 = date.today() + timedelta(days=2)
racion_de_3h = timedelta(hours=3)
ahora = datetime.now()
mas_3h = ahora + racion_de_3h

class Service(models.Model):
	hours         = models.CharField('Numero De horas',max_length=255, choices=CHOICES ,default='2')
	date_delivery = models.DateField('Fecha de Limpieza',default=datetime.now().strftime("%Y-%m-%d"))
	time_entry    = models.TimeField('Hora',default=mas_3h)
	direction     = models.CharField(max_length=5000)
	created       = models.DateTimeField(auto_now_add=True)
	owner         = models.ForeignKey(User, null=True, blank=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
	 	return str(self.date_delivery)

	def get_absolute_url(self):
		view_name = 'detail'
		return reverse(view_name,kwargs={'pk':self.id})
