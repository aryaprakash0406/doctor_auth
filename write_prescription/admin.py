from django.contrib import admin

from write_prescription.models import Prescription

@admin.register(Prescription)
class writePrescriptionModelAdmin(admin.ModelAdmin):
    list_display =('doctor_phoneNo','patient_phone','dignosed_with','medicines','symptoms','doses','when_to_eat','timing',)