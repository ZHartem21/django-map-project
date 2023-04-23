from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image_file = models.ImageField()
    number = models.IntegerField()

    def __str__(self):
        return f'{self.number} {self.place}'

