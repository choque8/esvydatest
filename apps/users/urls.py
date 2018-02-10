from django.conf.urls import patterns, include, url
from . import views
from django.contrib.auth.decorators import login_required


from apps.users.views import *

urlpatterns = [
    url(r'^logout/$', logout_, name='logout_'),
    url(r'^home$', views.home, name = 'home' ),
    url(r'^register', RegisterUser.as_view(), name = 'register' ), 
    url(r'^index', views.index, name = 'index' ),
    url(r'^list/$', ListPatient.as_view(), name="list_patient"),
    url(r'^new/$', newRelationMedicPatient.as_view(), name="new_relation"),
    url(r'^detail_patient/(?P<pk>\d+)$', DetailPatient.as_view(), name="detail_patient"),
    url(r'^edit/(?P<pk>.+)/$',EditPatient.as_view(), name="edit_patient"),
]
