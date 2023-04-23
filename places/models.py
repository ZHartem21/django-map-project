from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = HTMLField()
    description_long = HTMLField()
    lat = models.FloatField(max_length=100)
    lon = models.FloatField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['pk']

class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image_file = models.ImageField()
    number = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        ordering = ['number']