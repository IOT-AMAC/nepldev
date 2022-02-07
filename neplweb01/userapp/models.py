from django.db import models
from django import forms


class user_member(models.Model):
    objects = models.Manager()
    u_name = models.CharField(max_length=30)
    pswd = models.CharField(max_length=30)
    pswchdu = models.IntegerField()
    group_name = models.CharField(max_length=20)
    dept_name = models.CharField(max_length=20)
    status = models.CharField(max_length=20)


class eqp_list(models.Model):
    objects = models.Manager()
    eqp_name = models.CharField(max_length=30)
    eqp_type = models.CharField(max_length=30)
    param = models.CharField(max_length=30)
    sensors = models.IntegerField()
    log_inv = models.IntegerField()
    ip_addr = models.CharField(max_length=50)
    mach_code = models.IntegerField()
    eqp_status = models.CharField(max_length=30, default = "InActive")
    comment = models.CharField(max_length=50)


class eqp_data(models.Model):
    objects = models.Manager()
    eqp_name = models.CharField(max_length=30)
    ip_addr = models.CharField(max_length=50)
    conn_status = models.BooleanField()
    data = models.CharField(max_length=5000)

class admin_group(models.Model):
    objects = models.Manager()
    group_select = models.CharField(max_length=30)
    admin_page = models.BooleanField()
    supervise_page = models.BooleanField()
    audit_page = models.BooleanField()
    master_page = models.BooleanField()
    history_page = models.BooleanField()
    help_page = models.BooleanField()

class supervise_group(models.Model):
    objects = models.Manager()
    admin_page = models.BooleanField()
    supervise_page = models.BooleanField()
    audit_page = models.BooleanField()
    master_page = models.BooleanField()
    history_page = models.BooleanField()
    help_page = models.BooleanField()

class operator_group(models.Model):
    objects = models.Manager()
    admin_page = models.BooleanField()
    supervise_page = models.BooleanField()
    audit_page = models.BooleanField()
    master_page = models.BooleanField()
    history_page = models.BooleanField()
    help_page = models.BooleanField()