from typing import Any
from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Sensor,Measurement

from .serializers import  SensorSerializer, MeasurementSerializer, SensorDetatilSerializer

from django.http.response import JsonResponse, HttpResponse

from rest_framework import status

import json


class SensorView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
#добавление датчика
    def post(self,request):
        body = json.loads(request.body)
        t_data = SensorSerializer(data = body)
        if t_data.is_valid():
            t_data.save()
            return JsonResponse(t_data.data, status = status.HTTP_201_CREATED)
        return JsonResponse(t_data.errors, status = status.HTTP_400_BAD_REQUEST)


class SensorDetatilView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetatilSerializer
      #обновление сведений по датчику  
    def patch(self,request, pk, format = None):
        obj = self.queryset.get(id = pk)
        t_Ser = SensorSerializer(obj, data = request.data, partial = True)
        if t_Ser.is_valid():
            t_Ser.save()
            return JsonResponse(t_Ser.data, status = status.HTTP_200_OK)
        return JsonResponse(t_Ser.errors, status = status.HTTP_400_BAD_REQUEST)


class MeasurementView(ListAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
#добавление измерения для датчика
    def post(self,request):
        body = json.loads(request.body)
        t_data = MeasurementSerializer(data = body)
        if t_data.is_valid():
            t_data.save()
            return JsonResponse(t_data.data, status = status.HTTP_201_CREATED)
        return JsonResponse(t_data.errors, status = status.HTTP_400_BAD_REQUEST)
