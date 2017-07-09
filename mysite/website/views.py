from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from .forms import LoginForm, RegisterPerfilForm, RegisterUserForm, ContactanosForm, RecuperarPassForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction
from .models import Solicitud
from django.core.mail import send_mail



# Views de la app principal 'website' van aca.
def index(request):
	if request.user.is_authenticated:
		if request.user.perfil.es_supervisor:
			return render(request, 'website/index_user.html',{'base_template':'website/base_admin.html'})
		else:
			return render(request, 'website/index_user.html',{'base_template':'website/base_usuario.html'})
	else:
		loginf = LoginForm()	
		return render(request, 'website/index_noauth.html', {'loginf': loginf})

# View para autenticar usuarios e iniciar sesión
def logmein(request):
	
	form = LoginForm(request.POST or None)

	if request.POST and form.is_valid():
		user = form.login(request)
		if user:
			login(request, user)
			return HttpResponseRedirect('/')
	return render(request, 'website/index_noauth.html', {'loginf': form })

	
# View para cerrar la sesión de usuarios
def logmeout(request):
	logout(request)
	return HttpResponseRedirect('/')


	return render(request, 'website/index_noauth.html')


# View para desplegar el formulario de registro de usuarios y atender las peticiones de registro
def registrar(request):
	loginf = LoginForm()

	if request.method == 'POST':
		ruf = RegisterUserForm(request.POST, prefix='user')
		rpf = RegisterPerfilForm(request.POST, prefix='userprofile')
		if ruf.is_valid() * rpf.is_valid():
			user = ruf.save()
			userprofile = rpf.save(commit=False)
			userprofile.user = user
			userprofile.save()
			return HttpResponseRedirect('/')
		else:
			return render(request,'website/registrar.html', {'registeruserform':ruf, 'registerperfilform':rpf,'loginf': loginf})
	else:
		ruf = RegisterUserForm(prefix='user')
		rpf = RegisterPerfilForm(prefix='userprofile')
			#Si un usuario con sesión iniciada llega a esta página, se le cerrará la sesión.
		if request.user.is_authenticated:
			logout(request)

		return render(request, 'website/registrar.html', {'registeruserform':ruf, 'registerperfilform':rpf,'loginf': loginf})

def recuperar_pass(request):

	if request.method == 'POST':
		recuperarf = RecuperarPassForm(request.POST or None)
		if recuperarf.is_valid():
			print (recuperarf.email)	
		return HttpResponseRedirect('/')
	loginf = LoginForm()
	recuperarf = RecuperarPassForm()
	return render(request, 'website/recuperar_contraseña.html', {'recuperarf':recuperarf, 'loginf':loginf})

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
				return render(request, 'website/contacto.html',{'base_template':'website/base_admin.html','contactof':contactof})
			else:
				return render(request, 'website/contacto.html',{'base_template':'website/base_usuario.html','contactof':contactof})
		else:			
			loginf = LoginForm()	
			return render(request, 'website/contacto.html', {'base_template':'website/base.html','loginf': loginf,'contactof':contactof})


def descargas(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'website/descargas.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/descargas.html',{'base_template':'website/base_usuario.html'})

def descargas_materia(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'website/descarga_detalle.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/descarga_detalle.html',{'base_template':'website/base_usuario.html'})


def informacion(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'website/informacion.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/informacion.html',{'base_template':'website/base_usuario.html'})


def pedir_asesoria(request):
	 
	if request.user.perfil.es_supervisor:
		return render(request, 'website/pedir_asesoria.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/pedir_asesoria.html',{'base_template':'website/base_usuario.html'})

	
@login_required(login_url='/') 
def perfil(request):
	contexto_comun = {'nombre': request.user.first_name,\
	  				   'apellido': request.user.last_name,\
	  				   'email': request.user.email,\
	  				   'facultad': request.user.perfil.facultad,\
	  				   'desc': request.user.perfil.desc,\
	  				   'base_template':'website/base_usuario.html'\
	  				  }

	contexto_admin = {'nombre': request.user.first_name,\
	  				   'apellido': request.user.last_name,\
	  				   'email': request.user.email,\
	  				   'facultad': request.user.perfil.facultad,\
	  				   'desc': request.user.perfil.desc,\
	  				   'base_template':'website/base_admin.html'\
	  				  }

	if request.user.perfil.es_supervisor:
		return render(request, 'website/perfil.html',contexto_admin)
	else:
		return render(request, 'website/perfil.html',contexto_comun)


def sugerencia(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'website/sugerencia.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/sugerencia.html',{'base_template':'website/base_usuario.html'})

@login_required(login_url='/')
def solicitud_detalle(request,id_sol):
	if request.user.perfil.es_supervisor:
		#Buscamos las solicitudes libres

		solicitud = get_object_or_404(Solicitud, pk=id_sol)
		#solicitud = Solicitud.objects.get(pk=id_sol)

		return render(request, 'website/solicitud_detalle.html', {'solicitud':solicitud})
	
	raise Http404("Esta página no existe")

@login_required(login_url='/')
def administrar_solicitudes(request):

	if request.user.perfil.es_supervisor:
		#Buscamos las solicitudes libres

		libres = Solicitud.objects.filter(estado = 'Libre')
		contexto = {'solLibres':libres}
		return render(request, 'website/administrar_solicitudes.html',contexto)

	
	raise Http404("Esta página no existe")



