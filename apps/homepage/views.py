from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User
from django.conf import settings

from .models import LogService
#from .logForms import LogServiceForm

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self,request,*args,**kwargs):
		return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)

class ClassHistoryTemplateView(LoginRequiredMixin, TemplateView):
	template_name = "history.pug"
	def get_context_data(self, *args, **kwargs):
		context = super(ClassHistoryTemplateView, self).get_context_data(*args,**kwargs)
		context["titulo"]='Hola Mundo'
		return context

class Detail(DetailView):
	models = LogService

class ServiceListView(ListView):
	models = LogService
	def get_queryset(self, *args, **kwargs):
		qs = super(ServiceListView,self).get_queryset(*args,**kwargs)
		return qs


class Service(TemplateView):
	template_name='service.pug'
	def get_context_data(self, *args, **kwargs):
		context = super(ClassHistoryTemplateView, self).get_context_data(*args,**kwargs)
		context = {
			"el_titulo":'hola Mundo'
		}
		return context




# @login_required(login_url="/accounts/login/?next=/")
# def new_service_view(request):
# 	titulo="Nuevo Servicio"
# 	form =  LogServiceForm(request.POST or None)
# 	if form.is_valid():
# 		form_data = form.cleaned_data
# 		hou =form_data.get('hours')
# 		dat =form_data.get('date_delivery')
# 		tim =form_data.get('time_entry')
# 		die =form_data.get('direction')
# 		obj = LogServiceForm.objects.create(hours=hou, date_delivery=dat, time_entry=tim, direction=die)

# 	context = {
# 		"el_form":form,
# 		"titulo":titulo
# 	}
# 	return render(request,"loggame_form.pug",context)

	
# @login_required(login_url="/accounts/login/?next=/")
# def func_games(request):
#     games = serialize("json",LogGame.objects.all())
#     return HttpResponse(games, content_type="application/json")

@login_required(login_url="/accounts/login/?next=/")
def func_get_users(request):
	users = serialize("json",User.objects.all())
	return HttpResponse(users, content_type="application/json")
	