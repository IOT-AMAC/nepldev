from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import user_member, eqp_list, eqp_data, admin_group, supervise_group, operator_group

admin.site.register(user_member)
admin.site.register(eqp_list)
admin.site.register(eqp_data)
#admin.site.register(admin_group)
#admin.site.register(supervise_group)
#admin.site.register(operator_group)
