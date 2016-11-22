#from django.shortcuts import render,render_to_response
#from django.views.generic import TemplateView
#from django.template import RequestContext
# Create your views here.
#class index (TemplateView):
	#template_name = 'inicio/index.html'

#	def get(self, request, *args, **kwargs):
#		return render_to_response('inicio/index.html', context_instance = RequestContext(request))


from django.views.generic import TemplateView, FormView
from .forms import UserForm
from django.core.urlresolvers import reverse_lazy
from .models import Perfiles

class Registrarse(FormView):
	template_name = 'inicio/registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		perfil = Perfiles()
		perfil.usuario = user 
		perfil.cedula = form.cleaned_data['cedula']
		perfil.save()
		return super(Registrarse, self).form_valid(form)

