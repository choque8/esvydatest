from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from datetime import datetime
from django.utils import timezone



class Users(AbstractUser): 
    document = models.CharField(blank=True, null=True,max_length=40)
    born_date = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(blank=True, null=True,max_length=30)
    group = models.ForeignKey(Group, null=True)

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.username




class AppointmentState(models.Model):
    descrip = models.CharField(max_length=30)

    class Meta:
        db_table = 'estado_actividad'

    def __unicode__(self):
        return self.descrip


class Appointment(models.Model):
    name = models.CharField(max_length=30)
    descrip = models.TextField(blank=True, null=True)
    state = models.ForeignKey('AppointmentState', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    time  = models.TimeField(blank=True, null =True)
    medic = models.ForeignKey('Users', blank=True, null=True,related_name='medic')
    patient = models.ForeignKey('Users', blank=True, null=True,related_name='patient')
    first = models.NullBooleanField()

class AppointmentHistory:
    first = models.ForeignKey('Appointment', blank=True, null=True)
    control = models.ForeignKey('Appointment', blank=True, null=True)


class RelationMedicPatient(models.Model):

    medic = models.ForeignKey('Users', blank=True, null=True,related_name='medic_relation')
    patient = models.ForeignKey('Users', blank=True, null=True,related_name='patient_relation')




