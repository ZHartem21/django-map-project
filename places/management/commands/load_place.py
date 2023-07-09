from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image
import requests


class Command(BaseCommand):
    help = 'Helps to quickly create new place of interest'

    def load_place_images(self, image_url, place):
        response = requests.get(image_url)
        response.raise_for_status()
        image_name = response.url.split('/')[-1]
        image_content = ContentFile(response.content, name=image_name)
        image = Image.objects.create(place=place, image_file=image_content)
        self.stdout.write(self.style.SUCCESS(f'Created image for {image} '))

    def load_place_meta(self, place_file):
        response = requests.get(place_file)
        response.raise_for_status()
        place_details = response.json()
        if not place_details['title']:
            return
        place, created = Place.objects.get_or_create(
            title=place_details.get('title'),
            defaults={
                'description_short': place_details.get('description_short'),
                'description_long': place_details.get('description_long'),
                'lat': place_details.get('coordinates').get('lat'),
                'lon': place_details.get('coordinates').get('lng'),
            },
        )
        return place_details.get('imgs'), place, created

    def add_arguments(self, parser):
        parser.add_argument('file_address', nargs='+', type=str)

    def handle(self, *args, **options):
        for place_file in options['file_address']:
            place_image_urls, place, created = self.load_place_meta(place_file=place_file)
            for image_url in place_image_urls:
                self.load_place_images(image_url=image_url, place=place)

            self.stdout.write(self.style.SUCCESS(f'New: {created}. Created or updated place {place} '))
