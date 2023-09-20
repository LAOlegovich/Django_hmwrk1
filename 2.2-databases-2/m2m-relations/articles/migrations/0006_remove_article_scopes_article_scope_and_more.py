# Generated by Django 4.2.4 on 2023-09-20 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_rename_tags_article_scopes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
        migrations.AddField(
            model_name='article',
            name='scope',
            field=models.ManyToManyField(related_name='scope', through='articles.Articles_to_Tags', to='articles.tag'),
        ),
        migrations.AlterField(
            model_name='articles_to_tags',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag', verbose_name='Тэги'),
        ),
    ]
