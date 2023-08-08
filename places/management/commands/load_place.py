from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from places.models import Place, Image
from django.db.utils import IntegrityError
from django.core.exceptions import MultipleObjectsReturned
import requests


class Command(BaseCommand):
    help = 'Helps to quickly create new place of interest'

    def load_images(self, place_image_urls, place):
        try:
            for image_url in place_image_urls:
                response = requests.get(image_url)
                response.raise_for_status()
                image_name = response.url.split('/')[-1]
                image_content = ContentFile(response.content, name=image_name)
                image = Image.objects.create(place=place, image_file=image_content)
                self.stdout.write(self.style.SUCCESS(f'Created image for {image} '))
        except requests.exceptions.HTTPError:
            return

    def load_place(self, place_details):
        try:
            place, created = Place.objects.get_or_create(
                title=place_details['title'],
                defaults={
                    'description_short': place_details.get('description_short', 'No short description'),
                    'description_long': place_details.get('description_long', 'No long description'),
                    'lat': place_details['coordinates']['lat'],
                    'lon': place_details['coordinates']['lng'],
                },
            )
            return place_details.get('imgs', 'no-image'), place, created
        except (KeyError, TypeError, IntegrityError):
            self.stdout.write(self.style.ERROR('Failed to load place'))
            return

    def add_arguments(self, parser):
        parser.add_argument('file_address', nargs='+', type=str)

    def handle(self, *args, **options):
        try:
            for place_file in options['file_address']:
                response = requests.get(place_file)
                response.raise_for_status()
                place_details = response.json()
                place_image_urls, place, created = self.load_place(place_details=place_details)
                if not created:
                    raise MultipleObjectsReturned
                self.load_images(place_image_urls, place=place)
                self.stdout.write(self.style.SUCCESS(f'New: {created}. Created or updated place {place} '))
        except (KeyError, TypeError, IntegrityError, requests.exceptions.HTTPError):
            self.stdout.write(self.style.ERROR('Failed to create or update place'))
        except MultipleObjectsReturned:
            self.stdout.write(self.style.WARNING('Place already exists'))

