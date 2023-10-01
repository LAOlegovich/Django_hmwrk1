from rest_framework import serializers

from .models import Sensor,Measurement

class MeasurementSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Measurement
        fields = ['sens','value_temp','timestamp']
        #depth = 1 

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id','name','description']

class SensorDetatilSerializer(serializers.ModelSerializer):
    sens = MeasurementSerializer(many = True, read_only = True)
    class Meta:
        model = Sensor
        fields = ['id','name','description','sens']








