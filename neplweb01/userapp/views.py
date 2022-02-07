from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import user_member, eqp_list, eqp_data, admin_group, supervise_group, operator_group
from .forms import MemberForm, EqpCreation, AdminGroup, SuperviseGroup, OperatorGroup, EditUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
import json
from datetime import datetime
import paho.mqtt.client as mqtt
import ast

active_eqp_list = []
client = mqtt.Client()
client.connect("broker.hivemq.com", 1883, 60)

def home(request):

    client.on_connect = on_connect
    client.on_message = on_message
    client.loop_start()


    all_equip_data = list(eqp_data.objects.values())
    all_equip_list = list(eqp_list.objects.filter(eqp_status="Active").values())

    #print("all_equip_list  ", all_equip_list)
    #print(type(all_equip_list))
    #print(type(all_equip_list[0]))
    #print("all_equip_data   ", all_equip_data)
    #print("temp_dataaaaaaaa")
    temp_data = ast.literal_eval(all_equip_data[0]['data'])["temperature"]
    #print(temp_data)

    for i in range(0, len(all_equip_data)):
        for j in range(0, len(all_equip_list)):
            if all_equip_data[i]["ip_addr"] == all_equip_list[j]["ip_addr"]:
                try:
                    temp_data = ast.literal_eval(all_equip_data[i]['data'])["temperature"]
                    #print("temp_data")
                    #print(temp_data)
                    all_equip_list[j].update({"actual_temp":temp_data["actual_temp"]})
                    all_equip_list[j].update({"present_temp":temp_data["present_temp"]})
                    all_equip_list[j].update({"set_val":temp_data["set_val"]})
                    all_equip_list[j].update({"conn_status":all_equip_data[i]["conn_status"]})
                except:
                    print("errorrrrrrrrrrrrrrr")

    #print("all_equip_list  after adding", all_equip_list)

    all_members = user_member.objects.values()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()

    return render(request, 'index.html', {'all': all_members, 'allelist': all_equip_list, 'a':a, 's':s, 'o':o})


def on_connect(client, userdata, flags, rc):
    print("connected to broker " + str(rc))
    print("******************************************************")
    client.subscribe("nepl/dd")



def on_message(client, userdata, msg):
    if msg.topic == "nepl/dd":
        json_var=json.loads(msg.payload.decode())
        print(json_var)
        eq_data = eqp_data()
        eq_data.eqp_name = json_var["eqp_name"]
        eq_data.ip_addr = json_var["ip_addr"]
        eq_data.conn_status = json_var["conn_status"]
        eq_data.data = str(json_var["data"])
        eq_data.save()



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.success(request, 'Error logging in')
            return render(request, 'auth-login.html')
    else:

        return render(request, 'auth-login.html')


def register(request):
    if request.method == "POST":
        f = request.POST['group_name']
        print("dropdownnnnnn", f)
        #st = user_member.objects.get(u_name=f)
        #print("sssssssssss", st.u_name)
        #print("sssssssssss", st.pswd)
        form = MemberForm(request.POST or None)

        if form.is_valid():
            # print(form.data['u_name'])
            u_n = form.data['u_name']
            u_p = form.data['pswd']
            user = User.objects.create_user(u_n, None, u_p)
            form.save()
        all_members = user_member.objects.values()
        a = admin_group.objects.values().last()
        s = supervise_group.objects.values().last()
        o = operator_group.objects.values().last()
        # r = s[1]["group_name"]
        # print(r)
        return render(request, 'auth-register.html', {'all': all_members, 'a':a, 's':s, 'o':o})
    else:
        all_members = user_member.objects.values()
        a = admin_group.objects.values().last()
        s = supervise_group.objects.values().last()
        o = operator_group.objects.values().last()
        return render(request, 'auth-register.html',{'all': all_members, 'a':a, 's':s, 'o':o})


def edit_user(request):
    if request.method == "POST":
        f = request.POST['group_name']
        print("fffffffff",f)
        #print("dropdownnnnnn", f)
        #print("sssssssssss", s.u_name)
        #print("sssssssssss", s.pswd)
        form = EditUserForm(request.POST or None)
        #s = user_member.objects.get(u_name=f)
        print("formmmmmm",form.data["u_name"])
        if form.is_valid():
            print("hariiiiiiiiiiiiiiiiiiiiii")
            user_member.objects.filter(u_name=form.data["u_name"]).update(u_name = form.data["u_name"], pswd = form.data["pswd"], pswchdu = form.data["pswchdu"],group_name = form.data["group_name"], dept_name = form.data["dept_name"], status = form.data["status"]  )
            #form.save()
    all_members = user_member.objects.values()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()
    return render(request, 'auth-register.html', {'all': all_members, 'a':a, 's':s, 'o':o})


def user_secur(request):
    all_members = user_member.objects.values()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()
    return render(request, 'user_sec.html', {'all': all_members, 'a':a, 's':s, 'o':o})


def group_secur(request):
    all_members = user_member.objects.values()
    if request.method == "POST":
        form = AdminGroup(request.POST or None)
        print("admingroup", form.data)
        if(form.data["group_select"]=="ADMIN"):
            if form.is_valid():
                form.save()
        if (form.data["group_select"] == "SUPERVISOR"):
            f = SuperviseGroup(request.POST or None)
            print("supervisegroup", f.data)
            if f.is_valid():
                f.save()
        if (form.data["group_select"] == "OPERATOR"):
            f = OperatorGroup(request.POST or None)
            print("operatorrrrrrrrrrrrrrrr", f.data)
            if f.is_valid():
                f.save()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()

    return render(request, 'group_sec.html', {'all': all_members, 'a':a, 's':s, 'o':o})


def equip_create(request):
    all_members = user_member.objects.values()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()

    if request.method == "POST":
        form = EqpCreation(request.POST or None)
        print(form.data)
        ip=str(form.data["ip_addr1"])+"."+str(form.data["ip_addr2"])+"."+str(form.data["ip_addr3"])+"."+str(form.data["ip_addr4"])
        print(ip)
        if form.is_valid():
            f = form.save(commit=False)
            f.ip_addr=ip
            f.eqp_status = "Active"
            f.save()
            sink = datetime.now().isoformat().split('.')[0]
            client.publish("nepl/eqp_create_request", json.dumps({'ip_addr':f.ip_addr, 'log_interval':f.log_inv, 'eqp_name':f.eqp_name, 'eqp_status':f.eqp_status, 'sink':sink}))
            print("save")
        else:
            print("Not save")
            print(form.errors)
    return render(request, 'equip_creation.html', {'all': all_members, 'a':a, 's':s, 'o':o})

def eqp_param(request):
    all_members = user_member.objects.values()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()

    return render(request, 'eqp_param.html', {'all': all_members, 'a':a, 's':s, 'o':o})

def eqp_activ(request):
    all_members = user_member.objects.values()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()
    all_equip = eqp_list.objects.values()
    return render(request, 'eqp_activ.html', {'all': all_members, 'alle':all_equip, 'a':a, 's':s, 'o':o})

def his_rep(request):
    all_members = user_member.objects.values()
    a = admin_group.objects.values().last()
    s = supervise_group.objects.values().last()
    o = operator_group.objects.values().last()
    return render(request, 'his_rep.html', {'all': all_members, 'a':a, 's':s, 'o':o})



