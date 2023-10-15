# Generated by Django 4.2.4 on 2023-09-09 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('price', models.IntegerField(max_length=8, verbose_name='Цена')),
                ('image', models.ImageField(height_field=200, upload_to='', verbose_name='Изображение', width_field=200)),
                ('release_date', models.DateField(verbose_name='Дата выпуска')),
                ('lte_exists', models.BooleanField(verbose_name='Наличие LTE')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
        ),
    ]