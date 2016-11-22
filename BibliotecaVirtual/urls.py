from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BibliotecaVirtual.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #MOSTRAR IMAGEN
    url(r'^media/(?P<path>.*)$','django.views.static.serve', 
    	{'document_root': settings.MEDIA_ROOT,} ),

    #INICIO
    url(r'^', include('apps.inicio.urls')),

    #AUTORES
    url(r'^autor/', include('apps.autores.urls')),

    #LIBROS
    url(r'^libros/', include('apps.libros.urls')),
)
