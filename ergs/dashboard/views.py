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
from .serializers import userdata_dataSerializer,recharge_dataSerializer


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
# # from django.contrib.auth import authenticate
# # class HeroViewSet(viewsets.ModelViewSet):
# #     queryset = sensor_data.objects.all()
# #     serializer_class = Sensor_dataSerializer

class JSONResponse(HttpResponse):
    

    def __init__(self, data, **kwargs):
        permission_classes = (IsAuthenticated,)
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)
# @csrf_exempt
# def sensor_data_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
    
#     if request.method == 'GET':
#         sensor_data_list = sensor_data.objects.all()
#         serializer = Sensor_dataSerializer(sensor_data_list , many=True)
#         return JSONResponse(serializer.data)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         print(data)
#         print(type(data))
#         serializer = Sensor_dataSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=200)
#         return JSONResponse(serializer.errors, status=400)


#API to Receive and Register User data (Customer or Passsenger) from the vendor.
class userdata(APIView): 
    permission_classes = (IsAuthenticated,) 
    # def get(self, request):
    #     sensor_data_list = sensor_data.objects.all()
    #     serializer = Sensor_dataSerializer(sensor_data_list , many=True)
    #     return JSONResponse(serializer.data)

    def post(self,request): #Method for saving received user data registered to database
        data = JSONParser().parse(request)
        serializer = userdata_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)


#API to Recieve and verify vendor login data.
class vendor_verification(APIView): 
    permission_classes = (IsAuthenticated,)
    # def get(self, request):
    #     sensor_data_list = sensor_data.objects.all()
    #     serializer = vendor_verification_dataSerializer(sensor_data_list , many=True)
    #     return JSONResponse(serializer.data)

    def post(self,request): #Method for saving received sensor data to database
        data = JSONParser().parse(request)
        serializer = Sensor_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)


#API to Receive and Recharge amount for the customer or passenger.
class recharge(APIView): 
    permission_classes = (IsAuthenticated,)
    # def get(self, request):
    #     sensor_data_list = sensor_data.objects.all()
    #     serializer = vendor_verification_dataSerializer(sensor_data_list , many=True)
    #     return JSONResponse(serializer.data)

    def post(self,request): #Method for saving received sensor data to database

        data = JSONParser().parse(request)
        serializer = recharge_dataSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=200)
        return JSONResponse(serializer.errors, status=400)



#Login Function to Log in to the Administrative Dashboard
def login(request):   
    if request.method=="POST":
        username=request.POST["username"] 
        password = request.POST["password"]
        
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)  
            request.session['id']  = user.id
            request.method ="GET" 
            print(request.user.is_authenticated)   
            # relevant_data = relevant_data_fn(request)     
            print(request.user.is_authenticated)   
            # return render(request,'index-2.html',relevant_data)
            # return render(request,'index-2.html',relevant_data)
            messages.success(request, 'You logged in successfull')
            return HttpResponseRedirect('home')

        else:
            print(request.user.is_authenticated)
            # return render(request,'login-register.html')
            return render(request,'new_login.html')
    else:
        #  return render(request,'login-register.html')
        return render(request,'new_login.html')

@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True)
def home(request):
     relevant_data = relevant_data_fn(request) 
     return render(request,'index-2.html',relevant_data)



# # @login_required 
@cache_control(no_cache=True, must_revalidate=True) 
def relevant_data_fn(request):
    users= user_data.objects.all().count()
    cards_registered = all_available_card.objects.all().count()
    active_cards = 0 #later on to be fetched data from the database with active status from all cards
    non_active_cards = 0

    bus_location = bus_station.objects.values('station_name','centre_latitude','centre_longitude')
    location_list = list(bus_location)
    x = json.dumps(location_list)
    # active_cards=all_available_card.objects.filter(status__in='on').annotate(most_likes=Count('on')).order_by('most_likes')
    # active_cards=all_available_card.objects.
    
    # if active_cards_details == "on":
    #     active_cards = active_cards_details.count()
    # else:
    #     active_cards = 1 #later on to be fetched data from the database with active status from all cards
    # non_active_cards = 0
    relevant_data = {"number_of_cards": cards_registered,"users":users,"active_cards":active_cards,"non_active_cards":non_active_cards,"location_list":x}
    return relevant_data

# @cache_control(no_cache=True, must_revalidate=True) 
# def relevant_data_fn(request):
#     trains = train_detail.objects.all().count()
#     number_of_egates = gate_detail.objects.all().count()

#     active = get_todays_sales()
#     broken_egates = 1
#     bus_location = bus_station.objects.values('station_name','centre_latitude','centre_longitude')
#     location_list = list(bus_location)
#     x = json.dumps(location_list)
#     relevant_data = {"number_of_egates": number_of_egates,"trains":trains,"active":active,"broken_egates":broken_egates,"location_list":x}
#     return relevant_data

#insert a new Bus Station details
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def add_bus_station(request): 
    if request.method == 'POST':
        # district_located = request.POST['district_located']
        bus_station_details = bus_station()
        bus_station_details.station_id = request.POST.get('station_id')
        bus_station_details.station_name = request.POST.get('station_name')
        bus_station_details.centre_latitude =request.POST.get('centre_latitude')
        bus_station_details.centre_longitude =request.POST.get('centre_longitude')
        # bus_station_details.machine_id = request.POST.get('home_station')
        # bus_station_details.created_on = request.POST.get('train_type')
        # abus_station_details.station_of_origin = request.POST.get('origin')
        # abus_station_details.station_of_destination = request.POST.get('destination')
        try: 
            bus_station_details.save()
            messages.success(request,"Record Saved Successfully")
            return render(request,'bus-station-form.html',{})            
        except:
            messages.success(request,"Record Not Saved, There seems to be an error")
            return render(request,'bus-station-form.html',{})
    return render(request,'index-2.html')


#insert a new Vendor detail Station details
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def insert_vendor_data(request): 
    if request.method == 'POST':
        # district_located = request.POST['district_located']
        vendor_detail = vendor_data()
        vendor_detail.vendor_id = request.POST.get('vendor_id')
        vendor_detail.vendor_name = request.POST.get('vendor_name')
        vendor_detail.registration_number = request.POST.get('registration_number')
        vendor_detail.type_of_registration = request.POST.get('type_of_registration')
        vendor_detail.vendor_password = request.POST.get('password')
        # vendor_detail.date_created = request.POST.get('destination')
        try: 
            vendor_detail.save()
            messages.success(request,"Record Saved Successfully")
            return render(request,'vendor-form.html',{})            
        except:
            messages.success(request,"Record Not Saved, There seems to be an error")
            return render(request,'train-form.html',{})
    return render(request,'index-2.html')


#insert a new Recharge detail 
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def recharge_data(request): 
    if request.method == 'POST':
        # district_located = request.POST['district_located']
        recharge_detail = recharge()
        recharge_detail.uuid_number = request.POST.get('uuid_number')
        recharge_detail.recharged_amount = request.POST.get('phone_number')
        recharge_detail.place_of_recharge = request.POST.get('place_of_recharge')
        # vendor_detail.date_created = request.POST.get('destination')
        try: 
            recharge_detail.save()
            messages.success(request,"Record Saved Successfully")
            return render(request,'recharge-form.html',{})            
        except:
            messages.success(request,"Record Not Saved, There seems to be an error")
            return render(request,'recharge-form.html',{})
    return render(request,'index-2.html')


 
#insert a new Machine detail Station details
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def insert_machine_detail(request): #insert a new Machine detail Station details
    if request.method == 'POST':
        # district_located = request.POST['district_located']
        machine_detail = machine_on_bus_station()
        machine_detail.machine_id = request.POST.get('machine_id')
        machine_detail.status = request.POST.get('status')
        machine_detail.position = request.POST.get('position')
        machine_detail.amount_deducting = request.POST.get('amount_deducting')
        # vendor_detail.vendor_password = request.POST.get('password')
        # vendor_detail.date_created = request.POST.get('destination')
        try: 
            machine_detail.save()
            messages.success(request,"Record Saved Successfully")
            return render(request,'machineData-form.html',{})            
        except:
            messages.success(request,"Record Not Saved, There seems to be an error")
            return render(request,'train-form.html',{})
    return render(request,'index-2.html')


#insert a new user details via adminstrative daashboard.
@login_required(login_url='/admin_app/sumb')  #
@cache_control(no_cache=True, must_revalidate=True)  
def add_user_data(request): 
    if request.method == 'POST':
        # district_located = request.POST['district_located']
        user_detail = user_data()
        user_detail.user_name = request.POST.get('user_name')
        user_detail.uuid_number = request.POST.get('uuid_number')
        user_detail.national_id = request.POST.get('national_id') 
        user_detail.type_of_registration = request.POST.get('type_of_registration') 
        user_detail.vendor_id = request.POST.get('vendor_id')
        user_detail.phone_number = request.POST.get('phone_number') 

        try: 
            user_detail.save()
            messages.success(request,"Record Saved Successfully")
            # print (gate_details.west_sensor_longitude)
            return render(request,'user-form.html',{})            
        except:
            messages.success(request,"Record Not Saved, There seems to be an error")
            return render(request,'user-form.html',{})
    return render(request,'index-2.html')

# # @login_required ()
# def errorpage(request):
#     return render(request,'404.html',{ })

# @login_required(login_url='/sumb') 
# @cache_control(no_cache=True, must_revalidate=True) 
# def homepage(request):
#     if not request.user.is_authenticated:
#         return redirect('sumb')
#     users= user_data.objects.all().count()
#     cards_registered = all_available_card.objects.all().count()
#     active_cards_details=all_available_card.objects.values_list("status")
#     if active_cards_details == 'on':
#         active_cards = active_cards_details.count()
#     else:
#         active_cards = 0 #later on to be fetched data from the database with active status from all cards
#     non_active_cards = 0

    # cards_available=all_available_card.values_list()
    # titles = [" ", "Available cards","Active Cards","Non registered cards"]

    # a = type(cards_available)
    # # print(a)
    # a = list(cards_available)
    # # print(a)
    # coordinate_lat = []
    # coordinate_long = []
    # for i in a:
    #     coordinate_lat.append(i[2])
    #     coordinate_long.append (i[3])
        # print(i[2])
        # print(i[3])
        # # print(list(train_data))
        # print(coordinate_lat)
    return render (request,'index-2.html',{"number_of_egates": cards_registered,"trains":users,"active":active_cards,"broken_egates":non_active_cards})
    # else:
    #     return render(request,'login-register.html')

# @login_required(login_url='/sumb')
# @cache_control(no_cache=True, must_revalidate=True)  
# def trainupdate(request):
#     if not request.user.is_authenticated:
#         return redirect('sumb')
#     return render(request,'train-form.html',{})


#Redirecting to a  page for adding new bus station
@login_required(login_url='/admin_app/sumb')
@cache_control(no_cache=True, must_revalidate=True)  
def bus_station_form(request):
    if not request.user.is_authenticated:
        return redirect('sumb')
    return render(request,'bus-station-form.html',{})


#Redirecting to a Recharge form for top up customer account
@login_required(login_url='/admin_app/sumb')
@cache_control(no_cache=True, must_revalidate=True)  
def recharge_account(request):
    if not request.user.is_authenticated:
        return redirect('sumb')
    return render(request,'recharge-form.html',{})


#Redirecting to  a page for adding new Customer or passenger data (Registering card to a user) 
@login_required(login_url='/admin_app/sumb')
@cache_control(no_cache=True, must_revalidate=True)  
def customer_data(request):
    if not request.user.is_authenticated:
        return redirect('sumb')
    return render(request,'user-form.html',{})


#Redirecting to a page that add new Machine data (Registering Machines on bus station)
@login_required(login_url='/admin_app/sumb')
@cache_control(no_cache=True, must_revalidate=True)  
def add_machine_detail(request):
    if not request.user.is_authenticated:
        return redirect('sumb')
    return render(request,'machineData-form.html',{})

#Redirecting to a vendor form that registers new vendor 
@login_required(login_url='/admin_app/sumb')
@cache_control(no_cache=True, must_revalidate=True)  
def add_vendor_detail(request):
    if not request.user.is_authenticated:
        return redirect('sumb')
    return render(request,'vendor-form.html',{})
# # mzigo inapeleka data kwa trial-table ambayo lengo ni kuvuta id kwenye  <table id="data-table-basic" class="table table-striped"> 
# #pia kwenye static -> js -> data-table ->


# @login_required(login_url='/sumb') 
# def view_active_cards(request): #Getting data for Active Cards
#     if not request.user.is_authenticated:
#         return redirect('sumb')
#     doc_header = "Active Cards"
#     doc_para = "The Cards in use to Customer/Citizens"
#     titles = ["ID","Card Number","Status"]
#     active_cards_details=all_available_card.objects.values_list("status")
#     if active_cards_details == 'on':
        
#             # a = list(train)
#             # print (a[2])
#         return render(request,'table-trial.html',{"data":active_cards_details ,"data_tiles":titles,"doc_header":doc_header,"doc_para":doc_para })
#     # else:
#     return HttpResponse(request,'#') 


#Getting data of registers users (customer or passengers)
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def view_users(request):  # getting User data
    if not request.user.is_authenticated:
        return redirect('sumb')
    doc_header = "Users Registered"
    doc_para = "All Registered Users with cards currently in service"
    user_details=user_data.objects.values_list()
    titles = ["ID","Name","Card number","National ID","Type of Registration","Vendor ID","Phone Number","Balance Amount","Credit Amount","Date Created"]
    return render(request,'table-trial.html',{"data":user_details ,"data_tiles":titles,"doc_header":doc_header,"doc_para":doc_para})

#Getting data of Machines Registered 
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def machine_details(request): 
    if not request.user.is_authenticated:
        return redirect('sumb')
    doc_header = "Users Registered"
    doc_para = "All Registered Users with cards currently in service"
    machine_data=machine_on_bus_station.objects.values_list()
    titles = ["Machine ID","Status","Position","Amount Deducting","Bus Station","Date Created","Balance Amount","Credit Amount","Date Created"]
    return render(request,'table-trial.html',{"data":user_details ,"data_tiles":titles,"doc_header":doc_header,"doc_para":doc_para})

#Getting data of rgistered Bus stations
@login_required(login_url='/admin_app/sumb') 
def view_bus_station(request): #Getting Bus station data, Some data has to be fetched from the Machine table
    if not request.user.is_authenticated:
        return redirect('sumb')
    doc_header = "Bus Station"
    doc_para = "All currently Bus station"
    bus_station_details=bus_station.objects.values_list()
        
    titles = ["ID","Station Name","Station Registered Date  ","Machine Number","Machine's Position","Machine's Amount Deducting", "Registered Date of Machine "]
        # a = list(train)
        # print (a[2])
    return render(request,'table-trial.html',{"data":bus_station_details ,"data_tiles":titles,"doc_header":doc_header,"doc_para":doc_para })


#Getting data of Revenue collected 
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def view_bus_revenue(request):  # getting data from Fare collection Model, Some data to be fetched from Machine and Station.
    if not request.user.is_authenticated:
        return redirect('sumb')
    doc_header = "Revenue Collected"
    doc_para = "All Revenue Collected"
    revenue_details=fare_collection.objects.values_list()
    # titles = ["ID","Card Number","Station Name","Machine Number","Debit amount","Credit Amount","Date", "Total Debit Amount", "Total Credit Amount"]
    titles = ["ID","Card Number","Station Name","Machine Number","Debit amount","Credit Amount","Date"]
    return render(request,'table-trial.html',{"data":revenue_details ,"data_tiles":titles,"doc_header":doc_header,"doc_para":doc_para})

#Getting data of Registered Vendors
@login_required(login_url='/admin_app/sumb') 
@cache_control(no_cache=True, must_revalidate=True) 
def vendor_detail(request):  # getting data from Vendor Data Model, Some data to be fetched from Machine and Station.
    if not request.user.is_authenticated:
        return redirect('sumb')
    doc_header = "Registered Vendors"
    doc_para = "All the registered vendors"
    vendor_details=vendor_data.objects.values_list()
    titles = ["S/N","Vendor ID","Vendor name","Registration number","Registration type","Password","Date Registered"]

    return render(request,'table-trial.html',{"data":vendor_details ,"data_tiles":titles,"doc_header":doc_header,"doc_para":doc_para})



# @login_required(login_url='/sumb') 
# @cache_control(no_cache=True, must_revalidate=True)
# def sensor_data_raw(request): #Getting the sensor data
#     if not request.user.is_authenticated:
#         return redirect('sumb')
#     doc_header = "Sensor Data"
#     doc_para = "Sensor Data Recieved"
#     sensor=sensor_data.objects.values_list()
#     alldata = []
    
#     print(sensor)
#     for index, values in enumerate(sensor):
#         mxi = []
#         # print(list(values))
#         gatedata = gate_detail.objects.filter(id=list(values)[9]).values_list("Gate_name","zipcode","district","region","road_intersect_name")
#         # traindata = train_detail.objects.filter(id=gateid.train_id).value_list("id")
#         # print(gatedata)
#         if len(gatedata) > 0:
#             datavals = list(gatedata[0])
#             # print(type(datavals))
#             # print(datavals)
#             mxi = list(values) + datavals 
#             # print(values.index)
#         else: 
#             mxi = list(values)
#         alldata.append(mxi)
#     print(alldata)

#     # titles = ["ID","Gate Name", "Centre Latitude","Centre Longitude","East sensor Latitude","East sensor Longitude",
#     # "West sensor Latitude","West sensor Longitude","Zipcode","District","Region","Road Intersection Name"]
#     titles = ["Sensor ID","RFID Reading 1","RFID Reading 2", "Hall Effect Readings","Current Value 1","Currrent Value 2",
#     "Battery Health 1","Battery Health 2","Train ID","Gate ID","Created On","Gate Name","Zipcode","District","Region","Road Intersection Name"]

#     # # a = list(train)
#     # print (a)
#     return render(request,'table-trial.html',{"data": alldata ,"data_tiles":titles,"doc_header":doc_header,"doc_para":doc_para,"mzigo":"tatu" })

# # def map_render(data_values):   
# #     folium_map = folium.Map(location=[40.738, -73.98],
# #                             zoom_start=13,
# # #                            tiles="CartoDB dark_matter",
# #                             width='90%')
# #     fp

# #  for map view, will add the analytical data on network radius, network status, as well as location, train last detected where and other 
# #   matters.
# # 
# import ast
# import json
# from django.core.serializers.json import DjangoJSONEncoder

# def map_view(request):
#     a = {}
#     if User.is_authenticated:
#         trains = gate_detail.objects.values("gate_location")
#         a = list(trains)
#         values_list = []
#         for i in list(trains):
#             # print (i)
#             for d in i:
#                 # print(d)
#                 # print(i[d])
#                 a = ast.literal_eval(i[d])
#                 # print(type(a))
#                 # print(type(i[d]))
#                 # b= i[d]
#                 for k, v in a.items():
#                     if k == "coordinates":
#                         values_list.append([float(i) for i in v])
#                         # values_list.append(float(v))
#         # print(values_list)
#                 # for j in a:
#                 #     print(j)
#                 #     print(a[j])
#                 prices_json = json.dumps(values_list, cls=DjangoJSONEncoder)
#         return render(request,'mapview.html',{"locations":prices_json})
#     else:
#         return render(request,'login-register.html')


# @login_required(login_url='/sumb')
# @cache_control(no_cache=True, must_revalidate=True) 
# def secret_keys(request):
#     if not request.user.is_authenticated:
#         a = get_random_string(length=32)
#     return render(request,'dialog.html',{})

#Logout Function for Logged in user of the Adminstrative Dashboard
from django.contrib.auth import logout
@login_required
@cache_control(no_cache=True, must_revalidate=True) 
def logout_view(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # print(request.user.is_authenticated)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/admin_app/sumb')
