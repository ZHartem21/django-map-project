from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    description_short = models.TextField(blank=True, verbose_name='Короткое описание')
    description_long = HTMLField(blank=True, verbose_name='Длинное описание')
    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    class Meta:
        ordering = ['pk']
        unique_together = [['lat', 'lon']]

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True, related_name='images', verbose_name='Место')
    image_file = models.ImageField(verbose_name='Файл картинки')
    number = models.IntegerField(default=0, verbose_name='Номер порядка картинки')

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.place} ({self.number})'
