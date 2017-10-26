from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from material.frontend import urls as frontend_urls
from registration.backends.default.views import RegistrationView
from django.contrib.auth import views as auth_views

from apps.homepage.views import (
    Detail,
    ServiceListView,
    SeviceUpdateView,
    NewServiceView,
    ServiceDeleteView,
 )

from apps.washer.views import (
    HomeDoneView,
    NewWasherView,
    WasherListView,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^washer/', NewWasherView.as_view(), name="washeradd"),
    url(r'^washer_list/', WasherListView.as_view(), name="washer_list"),
    url(r'^done/', HomeDoneView.as_view(), name="done"),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^home$', ServiceListView.as_view(), name='home'),
    url(r'^detail/(?P<pk>\d+)/$', Detail.as_view(), name='detail'),
    url(r'^detail/(?P<pk>\d+)/update/$', SeviceUpdateView.as_view(), name='update'),
    url(r'^detail/(?P<pk>\d+)/delete/$', ServiceDeleteView.as_view(), name='delete'),
    url(r'^$', NewServiceView.as_view(), name='new_service'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Añadir Titulo admin
admin.site.site_header = 'Administración de WashMe'
