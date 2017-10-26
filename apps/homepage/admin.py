from django.contrib import admin
from .models import Service

from .models import Price

class AdminService(admin.ModelAdmin):
	list_display  = ['hours', 'date_delivery','time_entry','owner','the_whasher','direction']
	list_filter   = ["date_delivery", 'hours',  'the_whasher', 'owner']
	search_fields = ['direction']
	class Meta:
		model = Service
		
admin.site.register(Service,AdminService)
admin.site.register(Price)
#admin.site.register(Price)