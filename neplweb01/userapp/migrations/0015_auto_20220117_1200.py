# Generated by Django 3.2.9 on 2022-01-17 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0014_eqp_data'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='eqp_data',
            managers=[
            ],
        ),
        migrations.AddField(
            model_name='eqp_data',
            name='eqp_name',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
