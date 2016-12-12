from django.core.management.base import BaseCommand, CommandError
from ictus.models import *


class Command(BaseCommand):


    def handle(self, *args, **options):
        Paciente.objects.all().delete()
        Episodio.objects.all().delete()
        Basal.objects.all().delete()
