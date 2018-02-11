from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth.decorators import login_required
from apps.appointment.views import EditAppointment,DetailAppointment,NewAppointment,save_appointment,ListAppointmentPatient,cancel_appointment,NewControlAppointment,relation_appoint
from apps.appointment.views import ListAppointmentMedic
from apps.users.views import *

urlpatterns = [

    url(r'^new/(?P<pk>.+)/$',NewAppointment.as_view(), name="new_appointment"),
    url(r'^edit/(?P<pk>.+)/$',EditAppointment.as_view(), name="edit_appointment"),
    url(r'^details/(?P<pk>.+)/$',DetailAppointment.as_view(), name="detail_appointment"),
    url(r'^save/', save_appointment, name="save"),
    url(r'^list_pat/$', ListAppointmentPatient.as_view(), name="list_appointment_patient"),
    url(r'^list_appointment_medic/$', ListAppointmentMedic.as_view(), name="list_appointment_medic"),
    url(r'^cancel/$', cancel_appointment, name="cancel_appointment"),
    url(r'^new_control/(?P<pk>\d+)$', NewControlAppointment.as_view(), name="new_control"),
    url(r'^relation_appoint/$', relation_appoint ,name= 'relation'),
]   

