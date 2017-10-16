from django.contrib import admin
from .models import LogService

class AdminService(admin.ModelAdmin):
	list_display = ['hours', 'date_delivery','time_entry']
	list_filter = ["date_delivery",'hours']
	search_fields = ['hours', 'date_delivery', 'time_entry', 'direction']
	class Meta:
		model = LogService
		
admin.site.register(LogService,AdminService)

#, 'time_entry', 'direction'