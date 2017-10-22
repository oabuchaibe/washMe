from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
# Create your views here.
from django.shortcuts import render, redirect #puedes importar render_to_response
from apps.washer.forms import UploadForm
from apps.washer.models import Register
from material import (
    Layout, Fieldset, Row, Column, Span, Field,
    Span2, Span3, Span4, Span5, Span6, Span7,
    Span8, Span9, Span10, Span11, Span12,
    LayoutMixin)




class NewWasherView(CreateView):
   # template_name = 'washer/upload.html'

    model = Register
    form_class = UploadForm

    def get_success_url(self):
        return reverse('home')

    # def form_valid(self, form):
    #     form.instance.owner = self.request.user
    #     return super(NewServiceView, self).form_valid(form)

    # def get_form(self):
    #     form = super(NewServiceView, self).get_form(self.form_class)
    #     form.fields['date_delivery'].widget.attrs.update({'class': 'datepicker'})
    #     form.fields['time_entry'].widget.attrs.update({'class': 'timepicker'})
    #     form.fields['direction'].widget.attrs.update({'placeholder': 'Ingresa Una Ubicación'})
    #     form.fields['hours'].widget.attrs.update({'onchange': 'change()'})
    #     return form

    # def get_success_url(self):
    #     return reverse('home')

    # layout = Layout(
    #     Row('hours'),
    #     Row('date_delivery','time_entry'),
    #     Row('direction'),
    #     )














 
# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#         	newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
#         	newdoc.save(form)
#         	return redirect("uploads")
#     else:
#         form = UploadForm()
#     #tambien se puede utilizar render_to_response
#     #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
#     return render(request, 'wash/upload.html', {'form': form})