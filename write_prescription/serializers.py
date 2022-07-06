import imp
from pyexpat import model
from attr import fields
from rest_framework import serializers
from write_prescription.models import Prescription

class prescribe_medicineSrializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = ['doctor_phoneNo','patient_phone','dignosed_with','medicines','symptoms','doses','when_to_eat','timing',]