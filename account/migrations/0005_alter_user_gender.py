# Generated by Django 4.0.3 on 2022-06-13 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_user_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Gender',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
