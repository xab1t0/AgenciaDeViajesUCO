from django import forms

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	mensaje = forms.CharField(widget=forms.Textarea)
	email = forms.EmailField()

class ContactReserva(forms.Form):
	usuario = forms.CharField(required=True)
	hotel = forms.CharField(required=True)
	email = forms.EmailField()
