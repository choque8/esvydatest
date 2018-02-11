from django.contrib import admin

from apps.users.models import Users,AppointmentState,AppointmentHistory,RelationMedicPatient,Appointment

admin.site.register(Users)

admin.site.register(AppointmentState)
admin.site.register(RelationMedicPatient)
admin.site.register(Appointment)

