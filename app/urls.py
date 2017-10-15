from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from material.frontend import urls as frontend_urls

from apps.homepage.views import (
    ServiceListView,
	Service,
	Detail,
	ClassHistoryTemplateView,
	#NewService,
	func_get_users,
 )

urlpatterns = [
    url(r'^$', ClassHistoryTemplateView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),   
    url(r'^app/users$',func_get_users, name="users"),
    url(r'^service$', Service.as_view(), name='service'),
    url(r'^list$', ServiceListView.as_view(), name='list'),
    url(r'^detail/(?P<pk>\d+)/$', Detail.as_view(), name='detail'),


]
