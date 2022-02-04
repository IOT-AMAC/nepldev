from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import user_member, eqp_list, eqp_data

admin.site.register(user_member)
admin.site.register(eqp_list)
admin.site.register(eqp_data)