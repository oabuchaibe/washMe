from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from material.frontend import urls as frontend_urls

from apps.homepage.views import (
   #func_games,
   ClassHistoryTemplateView,
   new_service_view,
   func_get_users,
 )

urlpatterns = [
    url(r'^$', ClassHistoryTemplateView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('registration.backends.default.urls')),   
    url(r'^new_service$', new_service_view, name='log'),
    #url(r'^homepage/games$', func_games, name="games"),
    url(r'^app/users$',func_get_users, name="users"),
]
