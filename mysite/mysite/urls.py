"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from website import views as app_views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	
    #urls para autenticar via twitter
    url(r'^$', app_views.index, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^opciones/$', app_views.opciones, name='opciones'),
    url(r'^opciones/password/$', app_views.password, name='password'),

	   #urls para la app principal 'website' van aca.
	url(r'^', include('website.urls')),
        #urls para la app de 'descargas' van aca.
    url(r'^', include('descargas.urls')),
        #urls para la app de 'informacion' van aca.
    url(r'^', include('informacion.urls')),
]
