from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth.decorators import login_required

from apps.appointment.views import EditAppointment,DetailAppointment,NewAppointment,save_appointment,ListAppointmentPatient,cancel_appointment


from apps.users.views import *

urlpatterns = [
        #.....
    
    url(r'^new/(?P<pk>.+)/$',NewAppointment.as_view(), name="new_appointment"),
    url(r'^edit/(?P<pk>.+)/$',EditAppointment.as_view(), name="edit_appointment"),
    url(r'^details/(?P<pk>.+)/$',DetailAppointment.as_view(), name="detail_appointment"),
    url(r'^save/', save_appointment, name="save"),
    url(r'^list_pat/$', ListAppointmentPatient.as_view(), name="list_appointment_patient"),
    url(r'^cancel/$', cancel_appointment, name="cancel_appointment"),
]   

