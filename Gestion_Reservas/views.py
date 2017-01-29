from django.shortcuts import render, render_to_response, loader, HttpResponse
from django.http.response import HttpResponseRedirect
from django.template import RequestContext
from django import template
from forms import ReservaForm
from Usuario.models import Usuario
from Gestion_Reservas.models import Reservar

#View que muestra las reservas realizadas por cada usuario
def reservas(request):
	listaReservas = Reservar.objects.all()
	reservas = Reservar.objects.all().order_by('id')

	template = loader.get_template('Gestion_Reservas/reservas.html')
	context = {
		'listaReservas': listaReservas,
		'reservas': reservas,
	}
	return HttpResponse(template.render(context, request))

'''
# View de una reserva especifica
def reserva(request, reserva_id):
	listaReservas = Reservar.objects.all()
	datosReservas = Reservar.objects.get(pk=reserva_id)
  	template = loader.get_template('Gestion_Reservas/reserva.html')
	context = {
		'datosReservas': datosReservas,
	}
	return HttpResponse(template.render(context, request))


# View que permite la reserva del hotel elegido
def reservaHotel(request):
	if request.method == 'POST':
		form = ReservaForm(request.POST)
		if form.is_valid():
			form.save()
			hotel = request.POST['nombre_hotel']
			correo = request.POST['email']
			usuario = request.POST['nombre_usuario']
			reserva = Reservar.objects.get(nombre_hotel=hotel, nombre_usuario=usuario)
			reserva = Reservar.objects.create(email=correo)
			reserva.save()
			return HttpResponseRedirect('Gestion_Reservas/reservas.html')
	else:
		form = ReservaForm()
	template = loader.get_template('Gestion_Reservas/reservaHotel.html')
	context = {
		"el_form": form,
	}
	return HttpResponse(template.render(context, request))

'''
