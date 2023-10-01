from django.db import models


class Sensor(models.Model):
    id = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 20, unique= True, verbose_name='Имя')
    description = models.TextField(max_length= 2000, verbose_name='Описание')
    class Meta:
        ordering = ['id']

class Measurement(models.Model):
    id = models.AutoField(primary_key= True)
    value_temp = models.FloatField(verbose_name= 'Измеренная температура')
    timestamp = models.DateTimeField(auto_now= True, verbose_name= 'Дата-время измерения')
    sens = models.ForeignKey(Sensor,on_delete = models.CASCADE, related_name= 'sens')
    class Meta:
        ordering = ['id']



