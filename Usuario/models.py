from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
    nombre_Usuario = models.CharField(max_length=10) #Nombre del Usuario
    usuario = models.ForeignKey(User, blank=True) # Asignacion
    dinero_Usuario = models.IntegerField(default = 2000) # Dinero del Usuario

    def __str__(self):
        return self.nombre_Usuario
