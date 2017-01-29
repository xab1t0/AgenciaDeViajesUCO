from django import forms
from .models import Reservar

class ReservaForm(forms.ModelForm):
	class Meta:
		model = Reservar
		fields = ["nombre_hotel", "email", "nombre_usuario"]
