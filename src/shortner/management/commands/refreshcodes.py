from django.core.management.base import BaseCommand, CommandError
from shortner.models import ssurlURL

class Command(BaseCommand):
    help = 'refresh all ssurl shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        # print(options)
        return ssurlURL.objects.refresh_shorturl(options['items'])