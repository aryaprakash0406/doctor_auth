# Generated by Django 4.0.3 on 2022-06-13 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_user_tc_user_dob'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Gender',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
