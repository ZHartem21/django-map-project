from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image
import requests


class Command(BaseCommand):
    help = 'Helps to quickly create new place of interest'

    def add_arguments(self, parser):
        parser.add_argument('file_address', nargs='+', type=str)

    def handle(self, *args, **options):
        for place_file in options['file_address']:
            response = requests.get(place_file)
            response.raise_for_status()
            place_details = response.json()
            place, created = Place.objects.get_or_create(
                title=place_details['title'],
                description_short=place_details['description_short'],
                description_long=place_details['description_long'],
                lat=place_details['coordinates']['lat'],
                lon=place_details['coordinates']['lng'],
            )
            for image_url in place_details['imgs']:
                response = requests.get(image_url)
                response.raise_for_status()
                image_url_content = ContentFile(response.content)
                image = Image(place=place)
                image.save()
                image.image_file.save(response.url.split('/')[-1], image_url_content, save=True)
                self.stdout.write(self.style.SUCCESS(f'Created image for {image} '))

            self.stdout.write(self.style.SUCCESS(f'New: {created}. Created or updated place {place} '))