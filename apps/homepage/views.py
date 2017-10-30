from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Service
from .Forms import ServiceForm
from apps.washer.models import Register
from material import (
    Layout, Fieldset, Row, Column, Span, Field,
    Span2, Span3, Span4, Span5, Span6, Span7,
    Span8, Span9, Span10, Span11, Span12,
    LayoutMixin)

class LoginRequiredMixin(object):
	@method_decorator(login_required)
	def dispatch(self,request,*args,**kwargs):
		return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)

class StaffRequiredMixin(object):
	@method_decorator(staff_member_required)
	def dispatch(self,request,*args,**kwargs):
		return super(StaffRequiredMixin,self).dispatch(request,*args,**kwargs)

class Detail(DetailView):
	template_name = 'homepage/service_detail.pug'
	model = Service

class ServiceListView(ListView):
	#template_name  = 'homepage/service_list.pug'
	model = Service
	def get_queryset(self, *args, **kwargs):
		qs = super(ServiceListView,self).get_queryset(*args,**kwargs).filter(owner=self.request.user)
		return qs

class SeviceUpdateView(UpdateView):
	template_name = 'homepage/service_form.pug'
	model = Service
	form_class = ServiceForm

class ServiceDeleteView(DeleteView):
	template_name = 'homepage/service_confirm_delete.pug'
	model = Service
	def get_success_url(self):
		return reverse('home')

class NewServiceView(LayoutMixin,CreateView):
	#template_name = 'homepage/service_form.pug'
	model = Service
	form_class = ServiceForm
	def form_valid(self, form):
		instance = Register.objects.filter(status=True,working=False).first()
		if instance == None:
			porAsignar = Register.objects.get(id=2)
			form.instance.the_whasher = porAsignar
			form.instance.owner = self.request.user
		else:
			form.instance.the_whasher = instance
			form.instance.owner = self.request.user
			instance.working=True
			instance.save()
			
		return super(NewServiceView, self).form_valid(form)
	def get_form(self):
		form = super(NewServiceView, self).get_form(self.form_class)
		form.fields['date_delivery'].widget.attrs.update({'class': 'year'})
		form.fields['time_entry'].widget.attrs.update({'class': 'timepicker'})
		form.fields['direction'].widget.attrs.update({'placeholder': 'Ingresa Una Ubicación'})
		form.fields['hours'].widget.attrs.update({'onchange': 'myChangeFunction()'})
      

		return form
	def get_success_url(self):
		return reverse('home')
	layout = Layout(
		Row('hours',Fieldset('$ 0')),
		Row('date_delivery','time_entry'),
		Row('direction'),
		)

class HomeView(TemplateView):
	template_name =  'homepage/home_view.html'
	
class HomePayView(TemplateView):
	template_name =  'homepage/home_pay_view.html'


