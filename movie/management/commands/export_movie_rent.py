from django.core.management.base import BaseCommand, CommandError
import csv
from location.models import MoviesRent
from datetime import datetime

class Command(BaseCommand):


    def handle(self, *args, **options):
        
        with open('data/listing_movie_rent.csv', mode='w') as csv_file:
            fieldnames = ['fk_movie', 'fk_client', 'date_out', "i"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            i = 0
            for rent in MoviesRent.objects.all():
                if rent.date_return == None:
                    i += 1
                    writer.writerow({'fk_movie': rent.fk_movie, 'fk_client': rent.fk_client, 'date_out': rent.date_out, "i": i })





