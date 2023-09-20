from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length= 30, verbose_name= 'Tag')

    class Meta:
       verbose_name = 'Тэг'

    def __str__(self) -> str:
        return self.name  
    

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField('Tag', through ='Scope')


    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title




class Scope(models.Model):
    article = models.ForeignKey("Article", verbose_name="Статьи",related_name="scopes", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", verbose_name="Тэги", related_name="scopes", on_delete=models.CASCADE)
    is_main = models.BooleanField(verbose_name='Основной',  default= False)