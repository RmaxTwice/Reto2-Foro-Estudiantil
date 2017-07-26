from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required(login_url='/') 
def informacion(request):
	if request.user.perfil.es_supervisor:
		return render(request, 'informacion/informacion.html',{'base_template':'informacion/base_admin.html'})
	else:
		return render(request, 'informacion/informacion.html',{'base_template':'informacion/base_usuario.html'})