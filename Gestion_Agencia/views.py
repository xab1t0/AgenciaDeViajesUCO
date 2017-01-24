from django.shortcuts import render, HttpResponse, loader, redirect
from Gestion_Agencia.models import Ciudad, Avion, Hotel
from django import template

# View de la pagina principal.
def index(request):
	template = loader.get_template('Gestion_Agencia/index.html')
	context = {
	}
	return HttpResponse(template.render(context, request))

# View de la pagina de todas las ciudades.
def ciudades(request):
	listaCiudades = Ciudad.objects.all()
	ciudades = Ciudad.objects.all().order_by('nombre')
	
	template = loader.get_template('Gestion_Agencia/ciudades.html')
	context = {
		'listaCiudades': listaCiudades,
		'ciudades': ciudades,
	}
	return HttpResponse(template.render(context, request))

# View de una ciudad especifica
def ciudad(request, ciudad_id):
	listaCiudades = Ciudad.objects.all()
	datosCiudad = Ciudad.objects.get(pk=ciudad_id)
  	template = loader.get_template('Gestion_Agencia/ciudad.html')
	context = {
		'datosCiudad': datosCiudad,
	}
	return HttpResponse(template.render(context, request))

# View que muestra todos los vuelos.
def aviones(request):
	listaAviones = Avion.objects.all()
	aviones = Avion.objects.all().order_by('companyia')

	template = loader.get_template('Gestion_Agencia/aviones.html')
	context = {
		'listaAviones': listaAviones,
		'aviones': aviones,
	}
	return HttpResponse(template.render(context, request))

# View de un vuelo especifico.
def avion(request, avion_id):
	listaAviones = Avion.objects.all()
	datosAvion = Avion.objects.get(pk=avion_id)
	template = loader.get_template('Gestion_Agencia/avion.html')
	context = {
		'datosAvion': datosAvion,
	}
	return HttpResponse(template.render(context, request))

# View que muestra todos los hoteles.
def hoteles(request):
	listaHoteles = Hotel.objects.all()
	hoteles = Hotel.objects.all().order_by('ciudad')

	template = loader.get_template('Gestion_Agencia/hoteles.html')
	context = {
		'listaHoteles': listaHoteles,
		'hoteles': hoteles,
	}
	return HttpResponse(template.render(context, request))

# View de un hotel especifico.
def hotel(request, hotel_id):
	listaHoteles = Hotel.objects.all()
	datosHotel = Hotel.objects.get(pk=hotel_id)
	template = loader.get_template('Gestion_Agencia/hotel.html')
	context = {
		'datosHotel': datosHotel,
	}
	return HttpResponse(template.render(context, request))
