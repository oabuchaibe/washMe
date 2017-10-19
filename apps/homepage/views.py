from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required
from .models import Service
from .Forms import ServiceForm
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

# @login_required
# def home(request):
#     return render(request, 'homepage/service_list.pugl')

class Detail(LoginRequiredMixin,DetailView):
	template_name = 'homepage/service_detail.pug'
	model = Service


class ServiceListView(LoginRequiredMixin,ListView):
	template_name  = 'homepage/service_list.pug'
	model = Service

	def get_queryset(self, *args, **kwargs):
		qs = super(ServiceListView,self).get_queryset(*args,**kwargs)
		return qs

class SeviceUpdateView(LoginRequiredMixin,UpdateView):
	template_name = 'homepage/service_form.pug'
	model = Service
	form_class = ServiceForm

class ServiceDeleteView(LoginRequiredMixin,DeleteView):
	template_name = 'homepage/service_confirm_delete.pug'
	model = Service

	def get_success_url(self):
		return reverse('home')

class NewServiceView(LoginRequiredMixin,LayoutMixin,CreateView):
	
	template_name = 'homepage/service_form.pug'
	model = Service
	form_class = ServiceForm
	
	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super(NewServiceView, self).form_valid(form) 
		
	def get_form(self):
		#msj_direction_placeholder=_('address')
		form = super(NewServiceView, self).get_form(self.form_class)
		form.fields['date_delivery'].widget.attrs.update({'class': 'datepicker'})
		form.fields['time_entry'].widget.attrs.update({'class': 'timepicker'})
		#form.fields['direction'].widget.attrs.update({'onFocus': 'geolocate()'})
		#form.fields['direction'].widget.attrs.update({'placeholder': 'DIRECCIÓN'})
		return form

	def get_success_url(self):
		return reverse('home')

	layout = Layout(
		Row('hours'),
		Row('date_delivery','time_entry'),
		Row('direction'),
		)
	