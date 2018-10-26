# PRIMER TIPO PARA ENVIAR INFORMACIÓN
from django import forms
from apps.clientes.models import Cliente

class ClienteForm(forms.ModelForm):

	class Meta:
		# Esta clase va a tener las caracteristicas de nuestro formulario como tal
		model = Cliente

		fields = [
			'nombre',
			'apellidos',
			'fechaHBD',
			'numHijos',
        ]

		labels = {
			'nombre' : 'Nombre',
			'apellidos' : 'Apellidos',
			'fechaHBD' : 'Año de nacimiento',
			'numHijos' : 'Numero de Hijos',
		}

		widgets = {
			'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
			'apellidos' : forms.TextInput(attrs={'class': 'form-control'}),
			'fechaHBD' : forms.TextInput(attrs={'class': 'form-control'}),
			'numHijos' : forms.TextInput(attrs={'class': 'form-control'}),
		}