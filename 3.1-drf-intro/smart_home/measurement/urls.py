from django.urls import path

from .views import SensorView, MeasurementView,SensorDetatilView

urlpatterns = [
     path('sensors/', SensorView.as_view()),
     path('measurements/', MeasurementView.as_view()),
     #path('sensors/<pk>/', SensorView.as_view()),
     path('sensors/<pk>/', SensorDetatilView.as_view())
     

]
