from django.db import models
from django.contrib.auth.models import AbstractUser,Group
from datetime import datetime
from django.utils import timezone


class TypeDocument(models.Model):
    codigo = models.CharField(max_length=3)
    name = models.CharField(max_length=50, blank=True, null=True)
    descrip = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'type_document'

    def __unicode__(self):
        return self.name


class Users(AbstractUser):  #Usuario administrador. con Abstract user de django. (login desde web django)
    type_document = models.ForeignKey('TypeDocument', blank=True, null=True,db_column='type_document')
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