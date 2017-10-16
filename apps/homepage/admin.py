from django.contrib import admin
from .models import Service

class AdminService(admin.ModelAdmin):
	list_display = ['hours', 'date_delivery','time_entry']
	list_filter = ["date_delivery",'hours']
	search_fields = ['hours', 'date_delivery', 'time_entry', 'direction']
	class Meta:
		model = Service
		
admin.site.register(Service,AdminService)

