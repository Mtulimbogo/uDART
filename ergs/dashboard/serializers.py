from rest_framework import serializers
from .models import recharge
from .models import vendor_data,user_data

# class Sensor_dataSerializer(serializers.ModelSerializer):
class userdata_dataSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer to map the model instance to json format
    """
    user_name = serializers.CharField(max_length=220)
    uuid_number = serializers.CharField(max_length=220)
    national_id = serializers.IntegerField()
    type_of_registration = serializers.CharField(max_length=50) #whether adult or child
    vendor_id = serializers.CharField()
    current_amount = serializers.FloatField()
    credit_amount = serializers.FloatField()
    date_created = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    
    class Meta:
        model = user_data
        fields = ('id','user_name','uuid_number','national_id','type_of_registration',
        'vendor_id','current_amount','credit_amount','date_created')

class vendor_verification_dataSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer to map the model instance to json format
    """
    # vendor_id = serializers.CharField(max_length=6)
    # vendor_password = serializers.CharField(max_length=220)  

    # def login():
    #     username=vendor_id 
    #     password = vendor_password
    #     verify = vendor_data.objects.values_list('vendor_id','vendor_id')
    #     user = auth.authenticate(username = username,password = password)
              

    #     if user is not None:
    #         auth.login(request,user)  
    #         request.session['id']  = user.id
    #         request.method ="GET" 
    #         print(request.user.is_authenticated)   
    #         # relevant_data = relevant_data_fn(request)     
    #         print(request.user.is_authenticated)   
    #         # return render(request,'index-2.html',relevant_data)
    #         # return render(request,'index-2.html',relevant_data)
    #         messages.success(request, 'You logged in successfull')
    #         return HttpResponseRedirect('home')

    #     else:
    #         print(request.user.is_authenticated)
    #         return render(request,'login-register.html')
    # else:
    #      return render(request,'login-register.html')
    # class Meta:
    #     model = vendor_data
    #     fields = ('vendor_id','vendor_password')



       


class recharge_dataSerializer(serializers.HyperlinkedModelSerializer):
    """
    serializer to map the model instance to json format
    """
    uuid_number = serializers.IntegerField()
    recharged_amount = serializers.FloatField() 
    place_of_recharge = serializers.CharField(max_length=220)  
    date_of_recharge = serializers.DateTimeField(read_only=True, format="%Y-%m-%d")
    class Meta:
        model = recharge
        fields = ('uuid_number','recharged_amount','place_of_recharge','date_of_recharge')
    