from django import forms

from .models import LogGame


class LogForm(forms.ModelForm):

	class Meta:
		model = LogGame
		fields = ['game_date', 'yourScore', 'opponentScore', 'opponent']
		widgets = {
            'game_date': forms.TextInput(attrs={'class': 'datepicker'}),
            
            }