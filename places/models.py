from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = HTMLField()
    lat = models.FloatField(max_length=100)
    lon = models.FloatField(max_length=100)

    def __str__(self):
        return self.title   
    
    class Meta:
        ordering = ['pk']
        unique_together = [['lat', 'lon']]


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, null=True, blank=True)
    image_file = models.ImageField(null=True, blank=True)
    number = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        ordering = ['number']