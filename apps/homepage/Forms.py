from django import forms
from .models import Service
from .models import CHOICES


class ServiceForm(forms.ModelForm):

	class Meta:
		model = Service
		fields = ['hours', 'date_delivery', 'time_entry', 'direction' ]	
		widgets = {
            'date_delivery': forms.TextInput(attrs={'class': 'datepicker'}),
            'time_entry': forms.TextInput(attrs={'class':'timepicker'}),
            'hours': forms.Select(attrs={'class': 'browser-default'}),

            
            
        }

	