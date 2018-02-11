from django.conf.urls import url, include
from rest_framework import serializers
from apps.users.models import Appointment



class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ('name','descrip', 'state', 'date', 'time','medic', 'patient', 'first')
