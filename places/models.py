from django.db import models

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=200)
    description_short = models.TextField()
    description_long = models.TextField()
    lat = models.FloatField(max_length=100)
    lon = models.FloatField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
        verbose_name_plural = 'places'


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image_file = models.ImageField()
    number = models.IntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return f'{self.place}'

    class Meta:
        ordering = ['number']