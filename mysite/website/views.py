from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import LoginForm, RegisterPerfilForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import connection, transaction



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
			return render_to_response('website/registrar.html', {'registeruserform':ruf, 'registerperfilform':rpf,'loginf': loginf})
	else:
		ruf = RegisterUserForm(prefix='user')
		rpf = RegisterPerfilForm(prefix='userprofile')
		loginf = LoginForm()
			#Si un usuario con sesión iniciada llega a esta página, se le cerrará la sesión.
		if request.user.is_authenticated:
			logout(request)

		return render(request, 'website/registrar.html', {'registeruserform':ruf, 'registerperfilform':rpf,'loginf': loginf})




def contacto(request):
	if request.user.is_authenticated:
		if request.user.perfil.es_supervisor:
			return render(request, 'website/contacto.html',{'base_template':'website/base_admin.html'})
		else:
			return render(request, 'website/contacto.html',{'base_template':'website/base_usuario.html'})
	else:
		loginf = LoginForm()	
		return render(request, 'website/contacto.html', {'base_template':'website/base.html','loginf': loginf})


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

	
@login_required() 
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


def administrar_descargas(request):
	return render(request, 'website/administrar_descargas.html')

def administrar_solicitudes(request):
	
	return render(request, 'website/administrar_solicitudes.html')

def administrar_informacion(request):
	return render(request, 'website/administrar_informacion.html')
