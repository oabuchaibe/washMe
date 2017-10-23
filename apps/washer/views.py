from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.shortcuts import render, redirect 
from apps.washer.forms import UploadForm
from apps.washer.models import Register
from material import (
    Layout, Fieldset, Row, Column, Span, Field,
    Span2, Span3, Span4, Span5, Span6, Span7,
    Span8, Span9, Span10, Span11, Span12,
    LayoutMixin)


class NewWasherView(CreateView):
    model = Register
    form_class = UploadForm

    def form_valid(self, form):
        form.instance.status  = False
        form.instance.working = False
        
        return super(NewWasherView, self).form_valid(form)

    def get_form(self):
        form = super(NewWasherView, self).get_form(self.form_class)
        #form.fields['image'].widget.attrs.update({'class': 'btn-floating btn-large waves-effect waves-light red'})
        form.fields['birthday'].widget.attrs.update({'class': 'datepicker'})
        return form

    def get_success_url(self):
        return reverse('done')

    layout = Layout(
        Row('first_name','last_name'),
        Row('emiil','phone'),
        Row('birthday','sex'),
        Row('image'),
    )

class HomeDoneView(TemplateView):

    template_name = "washer/done.pug"