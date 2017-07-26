from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^sugerencia/$', views.sugerencia, name='sugerencia'),
    url(r'^pedir_asesoria/$', views.pedir_asesoria, name='pedir_asesoria'),
    url(r'^administrar_solicitudes/$', views.administrar_solicitudes, name='administrar_solicitudes'),
    url( r'^administrar_solicitudes/(?P<id_sol>\d+)/$', views.solicitud_detalle ,name='solicitud_detalles'),
    
]