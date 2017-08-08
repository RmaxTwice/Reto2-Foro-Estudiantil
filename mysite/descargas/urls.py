from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'descargas'
urlpatterns = [
    
    url(r'^descargas/facultad$', views.descargas, name='facultad'),
    url(r'^descargas/facultad/materia$', views.descargas_materia, name='materia'),
    
]