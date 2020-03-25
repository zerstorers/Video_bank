from django.core.management.base import BaseCommand, CommandError
from movie.models import Movies

class Command(BaseCommand):


    def handle(self, *args, **options):
        movies = Movies.object.all()
        for movie in movies:
            print(movie.name)