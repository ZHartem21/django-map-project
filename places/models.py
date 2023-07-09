from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField(blank=True, null=True)
    description_long = HTMLField(blank=True, null=True)
    lat = models.FloatField(max_length=100)
    lon = models.FloatField(max_length=100)

    class Meta:
        ordering = ['pk']
        unique_together = [['lat', 'lon']]

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True, related_name='images')
    image_file = models.ImageField()
    number = models.IntegerField(default=0)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.place} ({self.number})'
