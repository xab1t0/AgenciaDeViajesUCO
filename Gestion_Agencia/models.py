from __future__ import unicode_literals

from django.db import models

class Ciudad(models.Model):
	# Clase que contiene todas las ciudades
	nombre = models.CharField(max_length=200) #Nombre de las ciudades a elegir
	imagen = models.ImageField(upload_to='imagenes') #Imagen de la ciudad
	descripcion = models.TextField() #Descripcion de la ciudad
	valor_Ciudad = models.IntegerField(default = 0) #Indica el valor del paquete elegido

	def __str__(self):
		return self.nombre
		return self.imagen

class Hotel(models.Model):
    # Clase que contiene los hoteles de la ciudad
	nombre = models.CharField(max_length=200) #Nombre del Hotel
	ciudad = models.ForeignKey(Ciudad) #Relaciona Hotel con una Ciudad
	imagen = models.ImageField(upload_to='imagenes') #Imagen del Hotel
	descripcion = models.TextField() #Descripcion del Hotel
	valor = models.IntegerField(default = 0) #Valor de la habitacion del Hotel

	def __str__(self):
		return self.nombre
