# Generated by Django 4.0.3 on 2022-06-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_regdno_user_yearofadmission_user_medicalcouncil_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='YearOfAdmission',
        ),
    ]