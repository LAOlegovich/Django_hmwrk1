# Generated by Django 4.2.4 on 2023-09-20 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_articles_to_tags_article_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='scopes', through='articles.Articles_to_Tags', to='articles.tag'),
        ),
    ]