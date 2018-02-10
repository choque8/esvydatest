from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from datetime import datetime
from django.utils import timezone



class Users(AbstractUser):  #Usuario administrador. con Abstract user de django. (login desde web django)
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