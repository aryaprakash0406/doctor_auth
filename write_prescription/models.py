from operator import mod
from django.db import models

class Prescription(models.Model):
    # doctor_phoneNo=models.IntegerField()
    # patient_phone = models.IntegerField()
    # dignosed_with=models.CharField(max_length=200)
    # symptoms=models.CharField(max_length=200)
    # medicines=models.CharField(max_length=200)
    # doses=models.CharField(max_length=200)
    # when_to_eat=models.CharField(max_length=200)
    # # e.g morning
    # timing=models.CharField(max_length=200)


    doctor_phoneNo=models.CharField(max_length=100,null=True,blank=True)
    patient_phone = models.CharField(max_length=200,null=True,blank=True)
    dignosed_with=models.CharField(max_length=200,null=True,blank=True)
    symptoms=models.CharField(max_length=200,null=True,blank=True)
    medicines=models.CharField(max_length=200,null=True,blank=True)
    doses=models.CharField(max_length=200,null=True,blank=True)
    when_to_eat=models.CharField(max_length=200,null=True,blank=True)
    # e.g morning
    timing=models.CharField(max_length=200,null=True,blank=True)