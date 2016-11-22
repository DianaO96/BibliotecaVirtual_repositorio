from django.conf.urls import patterns, include, url
from .views import RegistrarAutor,ReportarAutor


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BibliotecaVirtual.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^registrar/$', RegistrarAutor.as_view() , name="registar_autor"),
    url(r'^reportar/$', ReportarAutor.as_view() , name="reportar_autor"),
   
)
