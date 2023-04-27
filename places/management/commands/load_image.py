from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile
from places.models import Place, Image
import requests


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('file_address', nargs='+', type=str)

    def handle(self, *args, **options):
        for image_url in options['file_address']:
            response = requests.get(image_url)
            response.raise_for_status()
            image_url_content = ContentFile(response.content)
            image = Image()
            image.save()
            image.image_file.save(response.url.split('/')[-1], image_url_content, save=True)
            self.stdout.write(self.style.SUCCESS(f'Created image {image} '))