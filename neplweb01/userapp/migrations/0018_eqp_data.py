# Generated by Django 3.2.9 on 2022-01-17 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0017_delete_eqp_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='eqp_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eqp_name', models.CharField(max_length=30)),
                ('ip_addr', models.CharField(max_length=50)),
                ('conn_status', models.BooleanField()),
                ('data', models.CharField(max_length=200)),
            ],
        ),
    ]
