from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrar/$', views.registrar, name='registrar'),
    url(r'^logmein/$', views.logmein, name='logmein'),
    url(r'^logmeout/$', views.logmeout, name='logmeout'),
    url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^descargas/facultad$', views.descargas, name='descargas'),
    url(r'^descargas/facultad/materia$', views.descargas_materia, name='descargas_detalle'),
    url(r'^informacion/$', views.informacion, name='informacion'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^sugerencia/$', views.sugerencia, name='sugerencia'),
    url(r'^pedir_asesoria/$', views.pedir_asesoria, name='pedir_asesoria'),
    url(r'^administrar_solicitudes/$', views.administrar_solicitudes, name='administrar_solicitudes'),
    url( r'^administrar_solicitudes/(?P<id_sol>\d+)/$', views.solicitud_detalle ,name='solicitud_detalles'),
]
