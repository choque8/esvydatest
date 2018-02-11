# encoding:utf-8
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from apps.users.models import Users, RelationMedicPatient
from apps.users.forms import RelationMedicPatientForm,EditUserForm

from django.views.generic import CreateView, ListView,DetailView,UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from apps.users.forms import RegisterForm


def index(request):
    
    return render(request, 'index.html', {})



def home(request):
    return render(request, 'index.html', {})


def logout_(request):
    """ Desloguearse de la plataforma """
    request.session.flush()
    #logout(request)
    return redirect('home')


class RegisterUser(SuccessMessageMixin,CreateView):
    model = Users
    template_name = "register.html"
    pk_url_kwarg = 'registerpk'
    form_class = RegisterForm
    success_url = reverse_lazy('home')
    additional_context = {}
    success_message = 'Usuario registrado satisfactoriamente'

class ListPatient(ListView):
    model = RelationMedicPatient
    template_name = 'users/list_patient.html'
    context_object_name = 'ListPatient'

class newRelationMedicPatient(CreateView):
    template_name = 'appointment/new_relation.html'
    form_class = RelationMedicPatientForm
    success_url = reverse_lazy('home')


class DetailPatient(DetailView):
    model = Users
    template_name = 'users/detail_patient.html'


class EditPatient(UpdateView):
    model = Users
    template_name = 'users/edit_patient.html'
    form_class = EditUserForm
    success_url = reverse_lazy('list_patient')