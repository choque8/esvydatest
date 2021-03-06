# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import CreateView, ListView,TemplateView, UpdateView
from django.views.generic.detail import DetailView

from apps.users.models import Appointment,RelationMedicPatient, Users,AppointmentState,AppointmentHistory
from apps.users.forms import RelationMedicPatientForm
from apps.appointment.forms import NewAppointmentForm

from django.core.urlresolvers import reverse_lazy
from apps.users.models import Appointment

from django.http import HttpResponse, JsonResponse
#from apps.appointment.serializers import AppointmentSerializer

class NewAppointment(CreateView):
    model = Appointment
    template_name = "appointment/new_appointment.html"
    pk_url_kwarg = 'registerpk'
    form_class = NewAppointmentForm
    success_url = reverse_lazy('home')
    additional_context = {}



class NewControlAppointment(DetailView):
    model = Appointment
    template_name = 'appointment/new_control_appointment.html'




class EditAppointment(UpdateView):
    model = Appointment
    template_name = 'proveedor.html'
    form_class = RelationMedicPatient
    success_url = reverse_lazy('productos:listado_proveedores')

class DetailAppointment(DetailView):
    model = Appointment
    template_name = 'detail_appointment.html'

def save_appointment(request):
    if request.method == 'GET':
        name = request.GET['name']
        descrip = request.GET['descrip']
        date = request.GET['date']
        time = request.GET['time']
        medicine = request.GET['medic']
        patient = request.GET['patient']
        state = AppointmentState.objects.get(id=1)
        medic = Users.objects.get(id=medicine)
        pati = Users.objects.get(id=patient) 

        result = Appointment.objects.filter(date = date).filter(time = time).filter(medic = medicine)
        if(result):
            #return last id inserted
            print result
            return JsonResponse("changedate", safe=False)

        else:
            print   "no encontró "
            query = Appointment(state = state,name=name, descrip=descrip ,date = date,time=time,medic=medic,patient=pati, first = True)
            query.save()
            #return last id inserted
            return JsonResponse(query.id, safe=False)

        


def relation_appoint(request):
    if request.method == 'GET':
        old = request.GET['old']
        new = request.GET['new']
        print "new ", new, "  old ", old
        if(new == "1"):
            old_appoint = Appointment.objects.get(id = old)
            query = AppointmentHistory(first = old_appoint)
            query.save()
        else:            
            old_appoint = Appointment.objects.get(id = old)
            new_appoint = Appointment.objects.get(id = new)
            query = AppointmentHistory(first = old_appoint,control=new_appoint)
            query.save()
    return JsonResponse("ok", safe=False)


def seeControlAppoint(request):
    if request.method == 'GET':
        id_appoint = request.GET['id']
        history = AppointmentHistory.objects.filter(control__id=id_appoint).order_by('-date')
        serializer = ActividadComentarioSerializer(histoyr, many=True)
        return JsonResponse(serializer.data, safe=False)



class ListAppointmentPatient(ListView):
    model = Appointment
    template_name = 'appointment/list_appointment_patient.html'
    context_object_name = 'ListAppointmentPatient'

    def dispatch(self, *args, **kwargs):
        return super(ListAppointmentPatient, self).dispatch(*args, **kwargs)  

    def get_queryset(self):
        queryset = Appointment.objects.filter(patient = self.request.user.id)
        return queryset


class ListAppointmentMedic(ListView):
    model = AppointmentHistory
    template_name = 'appointment/list_appointment_medic.html'
    context_object_name = 'ListAppointmentMedic'

    def dispatch(self, *args, **kwargs):
        return super(ListAppointmentMedic, self).dispatch(*args, **kwargs)  

    def get_queryset(self):
        queryset = AppointmentHistory.objects.filter(control__medic = self.request.user.id)
        return queryset



def cancel_appointment(request):
    if request.method == 'GET':
        appointment_id = request.GET['appointment_id']
        cancel = AppointmentState.objects.get(id = 2)
        Appointment.objects.filter(id=appointment_id).update(state=3)
    return JsonResponse("ok", safe=False)