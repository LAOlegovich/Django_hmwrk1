# Generated by Django 4.2.4 on 2023-09-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.IntegerField(db_index=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
