# encoding:utf-8
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from apps.users.models import Users
from django.views.generic import CreateView, ListView
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