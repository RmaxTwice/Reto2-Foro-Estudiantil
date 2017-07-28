from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve
from . import views


urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^registrar/$', views.registrar, name='registrar'),
    url(r'^logmein/$', views.logmein, name='logmein'),
    url(r'^logmeout/$', views.logmeout, name='logmeout'),
        
        #Views y urls para la recuperacion de passwords
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^desbloqueo/$', views.desbloquear_cuenta, name='desbloquear_cuenta'),
    url(r'^perfil/$', views.perfil, name='ver_perfil'),
    url(r'^perfil/editar$', views.perfil_editar, name='editar_perfil'),
    
]

# URL para servir las imagenes de forma local durante debug.

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT,}),
    ]