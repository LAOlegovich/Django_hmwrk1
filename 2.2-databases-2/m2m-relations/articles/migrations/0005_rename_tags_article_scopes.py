# Generated by Django 4.2.4 on 2023-09-20 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_tag_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='scopes',
        ),
    ]