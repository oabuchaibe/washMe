from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from .logForms import LogForm
from .models import LogGame
from django.contrib.auth.models import User
from django.conf import settings

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

@login_required(login_url="/accounts/login/?next=/")
def log_game_view(request):
	titulo="Log Game"
	form =  LogForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		gam =form_data.get("game_date")
		you =form_data.get("yourScore")
		oppS =form_data.get("opponentScore")
		opp =form_data.get("opponent")
		obj = LogGame.objects.create(game_date=gam, yourScore=you, opponentScore=oppS,opponent=opp)

	context = {
		"el_form":form,
		"titulo":titulo
	}
	return render(request,"loggame_form.pug",context)
	
@login_required(login_url="/accounts/login/?next=/")
def func_games(request):
    games = serialize("json",LogGame.objects.all())
    return HttpResponse(games, content_type="application/json")

@login_required(login_url="/accounts/login/?next=/")
def func_get_users(request):
	users = serialize("json",User.objects.all())
	return HttpResponse(users, content_type="application/json")
	