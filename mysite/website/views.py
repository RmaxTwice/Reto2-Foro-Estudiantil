from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout




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
					print('La cuenta de este usuario ha sido bloqueada!')
			else:
				print('El nombre de usuario o contraseña son inválidos!')


# View para cerrar la sesión de usuarios
def logmeout(request):
	logout(request)
	return HttpResponseRedirect('/')


	return render(request, 'website/index_noauth.html')

def adminview(request):
	return render(request, 'website/index_user_admin.html')

def registrar(request):
	return render(request, 'website/registrar.html')

def contacto(request):
	return render(request, 'website/contacto.html')

def descargas(request):
	return render(request, 'website/descargas.html')

def descargas_materia(request):
	return render(request, 'website/descarga_detalle.html')

def informacion(request):
	return render(request, 'website/informacion.html')

def pedir_asesoria(request):
	return render(request, 'website/pedir_asesoria.html')

def perfil(request):
	return render(request, 'website/perfil.html')

def sugerencia(request):
	return render(request, 'website/sugerencia.html')

def administrar_descargas(request):
	return render(request, 'website/administrar_descargas.html')

def administrar_solicitudes(request):
	return render(request, 'website/administrar_solicitudes.html')

def administrar_informacion(request):
	return render(request, 'website/administrar_informacion.html')

