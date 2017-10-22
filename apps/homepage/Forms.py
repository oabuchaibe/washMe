import goslate
import calendar
import pytz
from django import forms
from django.utils import timezone
from django.utils.translation import gettext as _
from .models import Service
from .models import CHOICES
from datetime import datetime, date, time, timedelta


tz = pytz.timezone('America/Bogota')
ct = datetime.now(tz=tz)
current_date = ct.strftime('%Y-%m-%d')
current_time = ct.strftime('%H:%M')
current_date_not_format = ct

racion_de_3h = timedelta(hours=3)
mas_3h = current_date_not_format + racion_de_3h
mas_3h = mas_3h.strftime('%H:%M')

racion_de_1d = timedelta(days=1)
mas_1d = current_date_not_format + racion_de_1d
mas_1d = mas_1d.strftime('%Y-%m-%d')



output = _('Seleccione una fecha correcta.')
msm_err = _('Seleccione una hora correcta.')
msm_hr = _('La hora seleccionada ya paso.')


class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ['hours', 'date_delivery', 'time_entry', 'direction']
	def clean_date_delivery(self):
		date_d = self.cleaned_data.get('date_delivery')
		horas_d = self.cleaned_data.get('hours')
		if str(date_d)< str(current_date):
			raise forms.ValidationError('No Hacemos Vijes en el Tiempo')
		if ((str(date_d)== str(current_date))):
			if (horas_d == '8'):
				raise forms.ValidationError('Servicios de Ocho Horas Reservar {}'.format(mas_1d))
			if ((horas_d == '2') and   (str(current_time) > '14:00' )):
				raise forms.ValidationError('Servicios de Dos Horas Reservar {}'.format(mas_1d))
			else:
				if ((horas_d == '3') and   (str(current_time) > '13:00' )):
					raise forms.ValidationError('Servicios de Tres Horas Reservar {}'.format(mas_1d))
		return date_d

	def clean_time_entry(self):
		time_e = self.cleaned_data.get('time_entry')
		date_d_t = self.cleaned_data.get('date_delivery')
		horas = self.cleaned_data.get('hours')
		if ((str(time_e)<('07:00:00')) or (str(time_e)>('09:00:00'))):
			if (horas == '8'):
				raise forms.ValidationError('Para Servicos De Ocho Horas 07:00 am - 09:00 am')
		if ((str(time_e)<('07:00:00')) or (str(time_e)>('16:00:00'))):
			if (horas == '3'):
				raise forms.ValidationError('Para Servicos De Tres Horas 07:00  - 16:00')
		if ((str(time_e)<('07:00:00')) or (str(time_e)>('17:00:00'))):
			if (horas == '2'):
				raise forms.ValidationError('Para Servicos De Tres Horas 07:00  - 17:00')
		if ((str(current_time)==str(time_e)) and ( str(current_date)== str(date_d_t))):
			raise forms.ValidationError(msm_err)
		if ((str(time_e)<str(current_time)) and (str(current_date)==str(date_d_t))):
			raise forms.ValidationError(msm_hr)
		if ((str(time_e) < str(mas_3h)) and ( str(current_date)== str(date_d_t))):
			raise forms.ValidationError(str('Para hoy hay servicios desde  {}'.format(mas_3h)))
		return time_e

#'horios 07:00 - 19:00'