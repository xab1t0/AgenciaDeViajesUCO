from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
app_name = 'Gestion_Agencia'
urlpatterns = [
	# ex: //
	url(r'^$', views.index, name='index'), #Pagina principal
	url(r'^ciudades/$', views.ciudades, name='ciudades'), #Pagina de todas las ciudades
	url(r'^ciudades/(?P<ciudad_id>[0-9]+)/$', views.ciudad, name='ciudad'), #Pagina de una ciudad
	url(r'^aviones/$', views.aviones, name='aviones'), #Pagina de todos los vuelos
	url(r'^aviones/(?P<avion_id>[0-9]+)/$', views.avion, name='avion'), #Pagina de un vuelo
	url(r'^hoteles/$', views.hoteles, name='hoteles'), #Pagina de todos los hoteles
	url(r'^hoteles/(?P<hotel_id>[0-9]+)/$', views.hotel, name='hotel'), #Pagina de un hotel
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
