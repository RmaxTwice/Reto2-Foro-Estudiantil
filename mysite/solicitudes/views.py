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
def solicitud_reservar(request,id_sol):
	if request.user.perfil.es_supervisor:
		
			#Buscamos las solicitud indicada a reservar en la base de datos.
		solicitud = get_object_or_404(Solicitud, pk=id_sol)
		#solicitud = Solicitud.objects.get(pk=id_sol)

			#Asignamos el supervisor que la reservo directo a la solicitud
		solicitud.supervisor = request.user

			# y alteramos su estado.
		solicitud.estado = 'Pendiente'
		solicitud.save()
		return HttpResponseRedirect('/administrar_solicitudes')
		#return render(request, 'solicitudes/solicitud_detalle.html', {'solicitud':solicitud})
	
	raise Http404("Esta página no existe")

@login_required(login_url='/')
def solicitud_liberar(request,id_sol):
	if request.user.perfil.es_supervisor:
		
			#Buscamos las solicitud indicada a liberar en la base de datos.
		solicitud = get_object_or_404(Solicitud, pk=id_sol)
		#solicitud = Solicitud.objects.get(pk=id_sol)

			#Desasignamos el supervisor de la solicitud
		solicitud.supervisor = None

			# y alteramos su estado.
		solicitud.estado = 'Libre'
		solicitud.save()
		return HttpResponseRedirect('/administrar_solicitudes')
		#return render(request, 'solicitudes/solicitud_detalle.html', {'solicitud':solicitud})
	
	raise Http404("Esta página no existe")

@login_required(login_url='/')
def solicitud_completa(request,id_sol):
	if request.user.perfil.es_supervisor:
		
			#Buscamos las solicitud indicada a liberar en la base de datos.
		solicitud = get_object_or_404(Solicitud, pk=id_sol)
		#solicitud = Solicitud.objects.get(pk=id_sol)

			# y alteramos su estado.
		solicitud.estado = 'Atendida'
		solicitud.save()
		return HttpResponseRedirect('/administrar_solicitudes')
		#return render(request, 'solicitudes/solicitud_detalle.html', {'solicitud':solicitud})
	
	raise Http404("Esta página no existe")


@login_required(login_url='/')
def administrar_solicitudes(request):

	if request.user.perfil.es_supervisor:
		#Buscamos las solicitudes libres

		libres = Solicitud.objects.filter(estado = 'Libre').order_by('fecha_enviado')
		pendientes = Solicitud.objects.filter(supervisor = request.user, estado = 'Pendiente').order_by('fecha_enviado')
		atendidas = Solicitud.objects.filter(supervisor = request.user, estado = 'Atendida').order_by('fecha_enviado')

		contexto = {'solLibres':libres, 'solReservadas': pendientes, 'solAtendidas': atendidas}
		return render(request, 'solicitudes/administrar_solicitudes.html',contexto)

	
	raise Http404("Esta página no existe")

