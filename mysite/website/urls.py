from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^registrar/$', views.registrar, name='registrar'),
    url(r'^indexu/$', views.logmein, name='logmein'),
    url(r'^indexa/$', views.adminview, name='adminbasic'),
    url(r'^descargas/$', views.descargas, name='descargas'),
    url(r'^informacion/$', views.informacion, name='informacion'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^sugerencia/$', views.sugerencia, name='sugerencia'),
    url(r'^pedir_asesoria/$', views.pedir_asesoria, name='pedir_asesoria'),
    url(r'^administrar_descargas/$', views.administrar_descargas, name='administrar_descargas'),
    url(r'^administrar_informacion/$', views.administrar_informacion, name='administrar_informacion'),
    url(r'^administrar_solicitudes/$', views.administrar_solicitudes, name='administrar_solicitudes'),
]
