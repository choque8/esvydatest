# encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.users.models import Users
from django.utils.translation import ugettext_lazy as _

class RegisterForm(UserCreationForm):
	class Meta:
		model = Users
		fields = [
			'group',
			'username',
			'first_name',
			'last_name',	
			'email',
			'document',
			'phone',
			'city',
			'born_date'

		]



		labels = { 
			'group' : 'Tipo de usuario',
			'username': 'Nombre de usuario',
			'first_name': 'Nombres',	
			'last_name': 'Apellidos',	
			'email': 'Correo',
			'document': 'Documento',
			'phone': 'Celular',
			'city': 'Ciudad',
			'born_date' :'Fecha de nacimiento',
		}