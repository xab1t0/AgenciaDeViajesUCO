from django.conf.urls import url, include
from django.conf import settings
from . import views
app_name = 'Reservas'
urlpatterns = [
    # ex: //
    #url(r'^reservaHotel/', views.reservaHotel, name='reservaHotel'), # Url que realiza la reserva del hotel y la asignacion del mismo a sus reservas
	url(r'^reservas/', views.reservas, name='reservas'), #Reservas de hoteles
]

