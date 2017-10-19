from django import forms
from .models import Service
from .models import CHOICES
from datetime import datetime, date, time, timedelta
import calendar
import pytz
from django.utils import timezone


from django.utils.translation import ugettext_lazy as _

tz = pytz.timezone('America/Bogota')
ct = datetime.now(tz=tz)
current_date = ct.strftime('%Y-%m-%d')
current_time = ct.strftime('%H:%M')
current_time_not_format = ct

racion_de_3h = timedelta(hours=3)
mas_3h = current_time_not_format + racion_de_3h
mas_3h = mas_3h.strftime('%H:%M')

output = _('name')

class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ['hours', 'date_delivery', 'time_entry', 'direction']	

	def clean_date_delivery(self):
		date_d = self.cleaned_data.get('date_delivery')
		if str(date_d)< str(current_date):
			raise forms.ValidationError(output)
		return date_d

	def clean_time_entry(self):
		time_e = self.cleaned_data.get('time_entry')
		date_d_t = self.cleaned_data.get('date_delivery')
		if ((str(current_time)==str(time_e)) and ( str(current_date)== str(date_d_t))):
			raise forms.ValidationError('No Hacemos viajes en el tiempo')
		if ((str(time_e)<str(current_time)) and (str(current_date)==str(date_d_t))):
			raise forms.ValidationError('No Hacemos viajes en el tiempo')
		if ((str(time_e) < str(mas_3h)) and ( str(current_date)== str(date_d_t))):
			raise forms.ValidationError(str('para hoy hay servicios desde  {}'.format(mas_3h)))

		return time_e
