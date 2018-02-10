# encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import Users,Appointment, RelationMedicPatient




class newAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['name', 'descrip', 'state', 'date','time', 'medic', 'patient']

    def __init__(self, *args, **kwargs):
        super(newAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Users.objects.all() 
        #self.fields['medic'].queryset = Users.objects.filter(grupo = 1) 
     
          

