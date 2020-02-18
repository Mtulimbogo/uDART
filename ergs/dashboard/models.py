from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.db import models
# from djgeojson.fields import PointField
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your models here.

class all_available_card(models.Model): #declare all the data of the card {that describes status}
    # id = models.AutoField(primary_key=True)
    uuid_number = models.IntegerField(primary_key = True)
    status = models.CharField(max_length=50)
      
    
    # api_token = get_random_string(length=32)

    def __str__(self):
        return str(self.uuid_number)

class user_data(models.Model): #Capturing user data
    # id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    uuid_number = models.IntegerField()
    national_id = models.IntegerField()
    type_of_registration = models.CharField(max_length=50) #whether adult or child
    vendor_id = models.CharField(max_length = 50,default = "")
    # recharge_balance = models.CharField(max_length= 50)
    current_amount = models.FloatField(max_length=220,default=0)#current_amount= ( (current_amount + total_amount_recharged) - credit_amount)
    # credit_amount = models.FloatField(max_length=220,default=0)#over deduction than the amount on the card
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

class fare_collection(models.Model): #Capturing user data
    # id = models.AutoField(primary_key=True)
    uuid_number = models.FloatField()
    credit_revenue = models.FloatField()
    debit_revenue = models.FloatField()
    machine_id = models.FloatField()
    # station_id =

    def __str__(self):
        return self.machine_id


class vendor_data(models.Model): #Capturing Vendor data 
    vendor_id = models.CharField(max_length=6,unique=True,default = "")
    vendor_name = models.CharField(max_length=50)
    registration_number = models.CharField(max_length = 50) #TIN for company or NIN for Individual 
    type_of_registration = models.CharField(max_length=50) #whether adult or child
    # recharge_balance = models.CharField(max_length= 50)
    vendor_password = models.CharField(max_length=10,default = "")
    date_created = models.DateTimeField(auto_now_add=True) 
    
    def __str__(self):
        return self.vendor_name

class machine_on_bus_station(models.Model):
    machine_id = models.IntegerField(primary_key = True)
    status = models.CharField(max_length=40)
    position = models.CharField(max_length=6)  #whether entry or exit 
    amount_deducting = models.FloatField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    # associated_bus_station = models.
    # amount_deducting = machine_id = models.IntegerField(max_length=50)
    def __str__(self):
        return self.machine_id
    # def __init__(self, *arg):
    #     super(admin_user, self).__init__()
    #     self.arg = arg

class bus_station(models.Model): #Provide the data of the Bus stop
    # id = models.AutoField(primary_key=True)
    station_id = models.IntegerField(primary_key = True)
    station_name = models.CharField(max_length=220)
    machine_id = models.ForeignKey(machine_on_bus_station, on_delete = models.CASCADE) 
    centre_latitude = models.FloatField(max_length=220,default=0) #recharge station ID
    centre_longitude = models.FloatField(max_length=220,default=0) #recharge station ID
    created_on = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.station_name


class recharge(models.Model):
    #Values that catches data interaction on Recharge point
    uuid_number = models.IntegerField()
    # initial_amount = models.FloatField(max_length=220,default=0)#current_amount
    recharged_amount = models.FloatField(max_length=220,default=0)#new amount deposition
    # total_amount_recharged = models.FloatField(max_length=220,default=0)#total_amount_recharged = initial_amount + recharged_amount
    place_of_recharge = models.CharField(max_length=220,default=0) #recharge station ID
    date_of_recharge = models.DateTimeField(auto_now_add=True) #Date of recharge
    
    def __str__(self):
        return self.place_of_recharge + ", Time: " + str(self.date_of_recharge)


class entry_log(models.Model): #interaction with the machines each time a commuter places a card on a machine
    #Values that catches data interaction on entry point
    uuid_number = models.IntegerField()
    entry_date_time = models.DateTimeField(auto_now_add=True)
    bus_station = models.CharField(max_length = 50)
    entry_amount_deducted = models.FloatField(max_length=220,default=0)
    
    def __str__(self):
        return self.bus_sation

class exit_log(models.Model):  
    #Values that catches data interaction on exit point
    uuid_number = models.IntegerField()
    exit_date_time = models.DateTimeField(auto_now_add=True)
    bus_station = models.CharField(max_length = 50)
    exit_amount_deducted = models.FloatField(max_length=220,default=0)
    
    def __str__(self):
        return self.bus_staion

class recharge_log(models.Model):
    #Values that catches data interaction on Recharge point
    uuid_number = models.IntegerField()
    initial_amount = models.FloatField(max_length=220,default=0)#current_amount
    recharged_amount = models.FloatField(max_length=220,default=0)#new amount deposition
    total_amount_recharged = models.FloatField(max_length=220,default=0)#total_amount_recharged = initial_amount + recharged_amount
    place_of_recharge = models.FloatField(max_length=220,default=0) #recharge station ID
    
    def __str__(self):
        return self.total_amount_recharged


# class Choice(models.Model):
#     question = models.ForeignKey(question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text