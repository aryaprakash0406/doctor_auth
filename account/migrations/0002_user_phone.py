# Generated by Django 4.0.3 on 2022-06-13 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]