from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^sugerencia/$', views.sugerencia, name='sugerencia'),
    url(r'^pedir_asesoria/$', views.pedir_asesoria, name='pedir_asesoria'),
    url(r'^administrar_solicitudes/$', views.administrar_solicitudes, name='administrar_solicitudes'),
    url( r'^administrar_solicitudes/(?P<id_sol>\d+)/$', views.solicitud_detalle ,name='solicitud_detalles'),
    url( r'^administrar_solicitudes/(?P<id_sol>\d+)/reservar$', views.solicitud_reservar ,name='solicitud_reservar'),
    url( r'^administrar_solicitudes/(?P<id_sol>\d+)/liberar$', views.solicitud_liberar ,name='solicitud_liberar'),
    url( r'^administrar_solicitudes/(?P<id_sol>\d+)/completa$', views.solicitud_completa ,name='solicitud_completa'),
]