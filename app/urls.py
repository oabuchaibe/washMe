from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from material.frontend import urls as frontend_urls

from django.contrib.auth import views as auth_views

from apps.homepage.views import (
    Detail,
    ServiceListView,
    SeviceUpdateView,
    NewServiceView,
    ServiceDeleteView,
 )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')), 
    url(r'^$', ServiceListView.as_view(), name='home'),
    url(r'^detail/(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    url(r'^detail/(?P<pk>\d+)/update/$', SeviceUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)/delete/$', ServiceDeleteView.as_view(), name='delete'),
    url(r'^new_service$', NewServiceView.as_view(), name='new_service'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
]

