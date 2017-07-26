from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from .forms import ContactanosForm
from .models import Solicitud
from website.forms import LoginForm

# Create your views here.

def contacto(request):
	if request.method == 'POST':
		cform = ContactanosForm(request.POST or None)
		if cform.is_valid():
			solicitud = cform.save(commit=False)
			solicitud.tipo = 'Contacto'
			solicitud.save()
			return HttpResponseRedirect('/')
		return HttpResponseRedirect('/contacto')
	else:
		contactof = ContactanosForm()
		if request.user.is_authenticated:
			if request.user.perfil.es_supervisor:
				return render(request, 'solicitudes/contacto.html',{'base_template':'solicitudes/base_admin.html','contactof':contactof})
			else:
				return render(request, 'solicitudes/contacto.html',{'base_template':'solicitudes/base_usuario.html','contactof':contactof})
		else:			
			loginf = LoginForm()	
			return render(request, 'solicitudes/contacto.html', {'base_template':'solicitudes/base.html','loginf': loginf,'contactof':contactof})


@login_required(login_url='/') 
def pedir_asesoria(request):
	 
	if request.user.perfil.es_supervisor:
		return render(request, 'solicitudes/pedir_asesoria.html',{'base_template':'solicitudes/base_admin.html'})
	else:
		return render(request, 'solicitudes/pedir_asesoria.html',{'base_template':'solicitudes/base_usuario.html'})

@login_required(login_url='/') 
def sugerencia(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'solicitudes/sugerencia.html',{'base_template':'solicitudes/base_admin.html'})
	else:
		return render(request, 'solicitudes/sugerencia.html',{'base_template':'solicitudes/base_usuario.html'})

@login_required(login_url='/')
def solicitud_detalle(request,id_sol):
	if request.user.perfil.es_supervisor:
		#Buscamos las solicitudes libres

		solicitud = get_object_or_404(Solicitud, pk=id_sol)
		#solicitud = Solicitud.objects.get(pk=id_sol)

		return render(request, 'solicitudes/solicitud_detalle.html', {'solicitud':solicitud})
	
	raise Http404("Esta página no existe")

@login_required(login_url='/')
def administrar_solicitudes(request):

	if request.user.perfil.es_supervisor:
		#Buscamos las solicitudes libres

		libres = Solicitud.objects.filter(estado = 'Libre')
		contexto = {'solLibres':libres}
		return render(request, 'solicitudes/administrar_solicitudes.html',contexto)

	
	raise Http404("Esta página no existe")

