from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import LoginForm, RegisterPerfilForm, RegisterUserForm
from django.contrib.auth import authenticate, login, logout
from django.db import connection, transaction



# Views de la app principal 'website' van aca.
def index(request):
	if request.user.is_authenticated:
		if request.user.perfil.es_supervisor:
			return render(request, 'website/index_user.html',{'base_template':'website/base_admin.html'})
		else:
			return render(request, 'website/index_user.html',{'base_template':'website/base_usuario.html'})
	else:
		form = LoginForm()	
		return render(request, 'website/index_noauth.html', {'form': form})

# View para autenticar usuarios e iniciar sesión
def logmein(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user = authenticate(username = u, password = p)
			if user is not None:
				if user.is_active:
					login(request , user)
					return HttpResponseRedirect('/')
				else:
					return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/')

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
		ruf = RegisterUserForm(prefix='user')
		rpf = RegisterPerfilForm(prefix='userprofile')
		return render(request, 'website/registrar.html', {'registeruserform':ruf, 'registerperfilform':rpf})

def contacto(request):
	return render(request, 'website/contacto.html')

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

	

def perfil(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'website/perfil.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/perfil.html',{'base_template':'website/base_usuario.html'})


def sugerencia(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'website/sugerencia.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/sugerencia.html',{'base_template':'website/base_usuario.html'})


def administrar_descargas(request):
	return render(request, 'website/administrar_descargas.html')

def administrar_solicitudes(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'website/descargas.html',{'base_template':'website/base_admin.html'})
	else:
		return render(request, 'website/descargas.html',{'base_template':'website/base_usuario.html'})

	return render(request, 'website/administrar_solicitudes.html')

def administrar_informacion(request):
	return render(request, 'website/administrar_informacion.html')
