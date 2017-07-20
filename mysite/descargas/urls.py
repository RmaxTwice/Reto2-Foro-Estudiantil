from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    
    url(r'^descargas/facultad$', views.descargas, name='descargas_principal'),
    url(r'^descargas/facultad/materia$', views.descargas_materia, name='descargas_detalle'),
    
]