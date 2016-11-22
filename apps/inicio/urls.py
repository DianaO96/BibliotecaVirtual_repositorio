from django.conf.urls import patterns, include, url
from .views import Registrarse

#from .views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BibliotecaVirtual.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

 # url(r'^$', index.as_view()),

 	url(r'^$','django.contrib.auth.views.login',{'template_name':'inicio/index.html'} , name='login'),	

 	url(r'^cerrar/$','django.contrib.auth.views.logout_then_login',name='logout'),

 	#url para registrarse 
 	url(r'^registrarse/$', Registrarse.as_view() , name = 'registrarse')
)
