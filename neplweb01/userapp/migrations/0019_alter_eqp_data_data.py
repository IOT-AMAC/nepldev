# Generated by Django 3.2.9 on 2022-01-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0018_eqp_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eqp_data',
            name='data',
            field=models.CharField(max_length=500),
        ),
    ]
