# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import CreateView, ListView,TemplateView, UpdateView
from django.views.generic.detail import DetailView

from apps.users.models import Appointment,RelationMedicPatient
from apps.users.forms import RelationMedicPatientForm
from django.core.urlresolvers import reverse_lazy



class EditAppointment(UpdateView):
    model = Appointment
    template_name = 'proveedor.html'
    form_class = RelationMedicPatient
    success_url = reverse_lazy('productos:listado_proveedores')

class DetailAppointment(DetailView):
    model = Appointment
    template_name = 'detail_appointment.html'
