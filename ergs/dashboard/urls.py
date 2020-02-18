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
app_name = "dashboard"
urlpatterns = [
#     # path('accounts/', include('django.contrib.auth.urls')),
    

#     # path(r'^login/$', views.login, {'template_name': '/login-register.html'}, name='login'),
#     path('error',views.errorpage, name = " 404 error"),
    path('Dashboard',views.home, name = " UDART dashboard"),
    path('view_users',views.view_users, name = "Retrieve users registered"),
    path('view_bus_station',views.view_bus_station, name = "Retrieve Bus station details"),
    path('view_bus_revenue',views.view_bus_revenue, name = "Retrieve revenue collected {from Fare collection}"),
    # path('view_active_cards',views.view_active_cards,name = "Retrieve the Actieve card {All registered}"),
    # path('view_machine_detail',views.view_machine_detail,name="Retrieve Machine Details"),
    path('add_bus_station',views.bus_station_form,name="Add Bus Details"),
    path('add_machine_detail',views.add_machine_detail,name="Add Machine Details"),
    path('add_vendor_detail',views.add_vendor_detail,name="Direct to Add vendor Details"),
    path('CustomerData', views.customer_data, name= "Retrieving form data for the customer/passenger"),
    path('vendor_data',views.insert_vendor_data,name="Insert vendor details to DB from form"),
    path('recharge_account',views.recharge_account,name="Control Number that allows user to recharge"),
    path('vendor_detail',views.vendor_detail,name="Retrieve Vendor Data"),
    path('apiyangu/user_data', views.userdata.as_view()), #API for inserting new user to DB
    path('api/vendor_verification', views.vendor_verification.as_view()), #API for authenticating the vendor once login to Account
    path('api/recharge', views.recharge.as_view()),#API for inserting new recharge balance from vendor to DB
    path('recharge', views.recharge_data, name = "add new gate to database"),
#     path('map_view',views.map_view, name= "System Map"),
#     path('key',views.secret_keys,name="Get api Token"),
    path('',views.login, name= "Welcome to UDART"),

    path('sumb',views.login, name= "Welcome to UDART"),
    path('home',views.home, name= "Welcome to UDART"),
#     #authentication routes....
#     # path('login',views.login, name= "Welcome to ERGS"),
#     url(r'^login$',views.login, name="test mzigo unaenda"),
    path('logout_view',views.logout_view,name="Logout"),
    
#     # path('', TemplateView.as_view(template_name='home.html'), name='home'), # new
    
#     path('register_view',views.register_view,name="Register"),
    
#     path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    
#     # path('', views.sensor_dataView.as_view(), name=None),
#     # patterns('',
#     # url(r'^data.geojson$', GeoJSONLayerView.as_view(model=WeatherStation), name='data'),
]
