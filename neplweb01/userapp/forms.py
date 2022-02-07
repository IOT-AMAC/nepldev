from django import forms
from .models import user_member, eqp_list, admin_group, supervise_group, operator_group


class MemberForm(forms.ModelForm):
    class Meta:
        model = user_member
        fields = ['u_name', 'pswd', 'pswchdu', 'group_name', 'dept_name', 'status']

class EditUserForm(forms.ModelForm):
    class Meta:
        model = user_member
        fields = ['u_name', 'pswd', 'pswchdu', 'group_name', 'dept_name', 'status']


class EqpCreation(forms.ModelForm):
    class Meta:
        model = eqp_list
        fields = ['eqp_name', 'eqp_type', 'param', 'sensors', 'log_inv', 'mach_code', 'comment']


class AdminGroup(forms.ModelForm):
    class Meta:
        model = admin_group
        fields = ['group_select', 'admin_page', 'supervise_page', 'audit_page', 'master_page', 'history_page', 'help_page']


class SuperviseGroup(forms.ModelForm):
    class Meta:
        model = supervise_group
        fields = ['admin_page', 'supervise_page', 'audit_page', 'master_page', 'history_page', 'help_page']


class OperatorGroup(forms.ModelForm):
    class Meta:
        model = operator_group
        fields = ['admin_page', 'supervise_page', 'audit_page', 'master_page', 'history_page', 'help_page']

