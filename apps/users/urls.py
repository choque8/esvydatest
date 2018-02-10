from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth.decorators import login_required


from apps.users.views import *

urlpatterns = [
    url(r'^login/$', login_, name='login_'),
    url(r'^logout/$', logout_, name='logout_'),
    url(r'^home$', login_required(views.home), name = 'home' ),
 
]
