from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpRequest
from dashboard.models import *
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder
import json
# # from .models import *
# # from django.contrib.auth import User
# # from django.contrib.auth.mixins import LoginRequiredMixin
# # from django.http import HttpRequest
# # Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
# from .models import train_detail
from django.contrib import messages,auth
from .models import *
from django.shortcuts import render, redirect,HttpResponse
# from .tables import TrainTable,GateTable
import folium
from django.utils.crypto import get_random_string
from rest_framework.permissions import IsAuthenticated


#Importing serializers for data saving API
# from .serializers import userdata_dataSerializer,recharge_dataSerializer


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout

#Import from dashboard app
from dashboard.views import add_user_data


# Create your views here.

def home(request):
    #  relevant_data = relevant_data_fn(request) 
     return render(request,'user-form.html')



def login(request):
    if request.method =="POST":
        username = request.POST.get("usrname")
        pwd = request.POST.get("pwd")

        print(username)
        print(pwd)
    return render(request,"login.html",{})

def check_login():
    return NotImplementedError

def vendor_setting(request):
    return render(request, "settings.html")

def recharge_tc(request):
         

    return render()

def register_tc(request):
    
    return render(request, "dashboard.html",{})

def change_pwd(request):
    return render (request, "changepwd.html",{})