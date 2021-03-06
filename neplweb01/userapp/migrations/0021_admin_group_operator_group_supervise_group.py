# Generated by Django 3.2.9 on 2022-02-05 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0020_alter_eqp_data_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_page', models.BooleanField()),
                ('supervise_page', models.BooleanField()),
                ('audit_page', models.BooleanField()),
                ('master_page', models.BooleanField()),
                ('history_page', models.BooleanField()),
                ('help_page', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='operator_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_page', models.BooleanField()),
                ('supervise_page', models.BooleanField()),
                ('audit_page', models.BooleanField()),
                ('master_page', models.BooleanField()),
                ('history_page', models.BooleanField()),
                ('help_page', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='supervise_group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_page', models.BooleanField()),
                ('supervise_page', models.BooleanField()),
                ('audit_page', models.BooleanField()),
                ('master_page', models.BooleanField()),
                ('history_page', models.BooleanField()),
                ('help_page', models.BooleanField()),
            ],
        ),
    ]
