from django import forms
from .models import Register


 

class UploadForm(forms.ModelForm):
	# filename = forms.CharField(max_length=100)
	# docfile = forms.FileField(
	# label='Selecciona un archivo'
	# )

	class Meta:
		model = Register
		fields = ['filename','docfile']