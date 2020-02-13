# from rest_framework import serializers
# from ..models import sensor_data

# class Sensor_dataSerializer(serializers.ModelSerializer):
#     """
#     serializer to map the model instance to json format
#     """
# class Meta:
#     model = sensor_data
#     fields = ('id','rfid1_readings','rfid2_readings',
#     'hall_effect_readings','current_values1','current_values2','battery_health1',
#     'battery_health2','train_id','gate_id')