from django import forms
from .models import LogService




class LogServiceForm(forms.ModelForm):
	class Meta:
		model = LogService
		fields = ['hours', 'date_delivery', 'time_entry', 'direction']
		widgets = {
            'date_delivery': forms.TextInput(attrs={'class': 'datepicker'}),
            'time_entry': forms.TextInput(attrs={'class':'timepicker'})
            }

