from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth.decorators import login_required

from apps.appointment.views import EditAppointment,DetailAppointment


from apps.users.views import *

urlpatterns = [
        #.....
    
    url(r'^edit/(?P<pk>.+)/$',EditAppointment.as_view(), name="edit_appointment"),
    url(r'^details/(?P<pk>.+)/$',DetailAppointment.as_view(), name="detail_appointment"),
]   

