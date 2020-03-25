from django.core.management.base import BaseCommand, CommandError
import csv
from movie.models import Movies
from datetime import datetime

class Command(BaseCommand):


    def handle(self, *args, **options):
        with open('data/netflix_titles.csv', 'r') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            Movies.objects.all().delete()
            for row in reader:
                netflix_id, typ, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description = row
                # print(netflix_id, typ, title, director, cast, country, date_added, release_year, rating, duration, listed_in, descripton)

                # release_year_object = datetime.strptime(release_year, '%Y')
                lol = date_added.replace(",", "")
                date_added_object = datetime.strptime(lol, '%B %d %Y')
                duration_int = int(duration.split(" ")[0])

                Movies.objects.create(
                name=title,
                description=description,
                date=date_added_object ,
                actors=cast,
                country=country,
                director=director,
                length=duration_int,

            )

