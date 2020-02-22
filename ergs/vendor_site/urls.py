from django.urls import path,include
# from django.shortcuts import url
from django.contrib.auth import authenticate

from dashboard import views
from djgeojson.views import GeoJSONLayerView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views
from rest_framework import routers
# from .api import views
from django.views.generic.base import TemplateView # new
from django.contrib.auth import views as auth_views
from django.conf.urls import url
app_name = "vendor_site"
urlpatterns = [

     path('', views.login, name ="Login Page" ),
     path("login", views.login, name ="Login Page" ),
     path('dashboard', views.register_tc, name = "Register Transport Card"),
     path("vendor_setting", views.vendor_setting, name="Vendor Setting"),
     path("changepwd",views.change_pwd, name = "Change Vendor Password"),
 

]