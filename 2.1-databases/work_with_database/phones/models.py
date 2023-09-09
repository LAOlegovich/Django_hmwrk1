from django.db import models
from django.urls import reverse



class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key = True, db_index = True)
    name = models.CharField(max_length=50, unique = True, verbose_name= 'Имя')
    price = models.FloatField(verbose_name = 'Цена',)
    image = models.CharField(max_length=100, verbose_name= 'Ссылка')
    release_date = models.DateField(verbose_name = 'Дата выпуска')
    lte_exists = models.BooleanField(verbose_name = 'Наличие LTE')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name="URL")

    def get_p(self,par):
        if par == "name":
            return self.name
        else:
            return self.price