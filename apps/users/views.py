# encoding:utf-8
from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from apps.users.models import Users
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin


def login_(request):
    """ Login personalizado de la plataforma, no permite usuarios inactivos y
    usuario no aprobados """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)

                else:
                    messages.error(request, (
                        'No esta autorizado para ingresar a la plataforma'))
                    return redirect(reverse('inicio', args=()))
            else:
                messages.error(request, (
                    'El usuario o la contraseña son incorrectos'))
                return redirect(reverse('inicio', args=()))
    return redirect('inicio')





def home(request):
    return render(request, 'index.html', {})


def logout_(request):
    """ Desloguearse de la plataforma """
    request.session.flush()
    #logout(request)
    return redirect('inicio')
