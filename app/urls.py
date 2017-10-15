from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from material.frontend import urls as frontend_urls

from apps.homepage.views import (
    Detail,
    ServiceListView,
	
    NewServiceView,
 )

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),   
    

    url(r'^detail/(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    url(r'^$', ServiceListView.as_view(), name='home'),

    url(r'^new_service$', NewServiceView.as_view(), name='new_service'),
    


]
