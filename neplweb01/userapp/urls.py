from django.urls import path
from . import views

urlpatterns = [

    path('home', views.home, name="dashboard-page"),
    path('', views.user_login, name="login-page"),
    path('login', views.user_login, name="login-page"),
    path('register', views.register, name="User Creation Page"),
    path('group_security', views.group_secur, name="Group Security Page"),
    path('user_security', views.user_secur, name="User Security Page"),
    path('create_equipment', views.equip_create, name="Equipment Creation"),
    path('eqp_parameter', views.eqp_param, name='Equipment Parameter'),
    path('eqp_activation', views.eqp_activ, name='Equipment Activation Page'),
    path('his_rep', views.his_rep, name='History Data Report'),
    path('edit_user', views.edit_user, name='Edit User')

]
