from __future__ import unicode_literals
from django.db import models
from Gestion_Agencia.models import Hotel
from Usuario.models import Usuario

class Reservar(models.Model):
	nombre_hotel = models.ForeignKey(Hotel)
	email = models.EmailField()
	nombre_usuario = models.ForeignKey(Usuario)

	def __str__(self):
		return self.email
