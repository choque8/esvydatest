# encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import Users,Appointment, RelationMedicPatient



class NewAppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = ['name', 'descrip', 'state', 'date','time', 'medic', 'patient']

    def __init__(self, *args, **kwargs):
        super(NewAppointmentForm, self).__init__(*args, **kwargs)
        self.fields['patient'].queryset = Users.objects.all() .filter(group = 2)  
        self.fields['medic'].queryset = Users.objects.filter(group = 1) 
