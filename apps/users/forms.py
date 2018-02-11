# encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from apps.users.models import Users, RelationMedicPatient
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



class EditUserForm(forms.ModelForm):

    class Meta:
        model = Users
        fields = ['group', 'first_name', 'last_name', 'email','document', 'phone', 'city', 'born_date']


class RelationMedicPatientForm(forms.ModelForm):

    class Meta:
        model = RelationMedicPatient
        fields = ['medic', 'patient']

    def __init__(self, *args, **kwargs):
        super(newAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Users.objects.filter(group = 2)  
        self.fields['medic'].queryset = Users.objects.filter(group = 1)       		