from django import forms
from registration.forms import RegistrationForm
#from .models import UserProfile

# CHOICES = (
#         ('2', 'Dos Horas'),
#         ('3', 'Tres Horas'),
#         ('8', 'Ocho Horas'),
#         )
 
# class ExRegistrationForm(RegistrationForm):
#     is_human = forms.ChoiceField(choices=CHOICES, label = "Are you human?:")

# class UserProfileForm(RegistrationForm):
#     website = forms.URLField(max_length=200,help_text='Please entre the url of the page')
#     picture = forms.ImageField()
#     class Meta:
#         model = UserProfile
#         fields = '__all__'
# from registration.forms import RegistrationForm
# from django import forms
 
# class ExRegistrationForm(RegistrationForm):
#     is_washer = forms.ChoiceField(label = "Are you human?:")