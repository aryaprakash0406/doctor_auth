# Generated by Django 4.0.3 on 2022-06-15 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write_prescription', '0006_delete_medicine_prescription_medicines'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='doctor_phoneNo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
