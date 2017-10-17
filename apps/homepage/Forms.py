from django import forms
from .models import Service
from .models import CHOICES
from datetime import datetime, date, time, timedelta
import calendar
import pytz
from django.utils import timezone


class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = ['hours', 'date_delivery', 'time_entry', 'direction']	
		widgets = {
            'date_delivery': forms.DateInput(attrs={'class': 'datepicker'}),
            'time_entry': forms.TimeInput(attrs={'class':'timepicker'}),
            'hours': forms.Select(attrs={'class': 'browser-default'}),
        }


	def clean_date_delivery(self):
		date_d = self.cleaned_data.get('date_delivery')
		tz = pytz.timezone('America/Bogota')
		ct = datetime.now(tz=tz)
		current_date = ct.strftime("%Y-%m-%d")
		if ( str(date_d)  < str(current_date) ):
			raise forms.ValidationError('no hacemos viajes en el tiempo')
		return date_d

	#def cleaned_	
