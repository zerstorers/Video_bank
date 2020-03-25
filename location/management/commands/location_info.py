from django.core.management.base import BaseCommand, CommandError
from location.models import MoviesRent
from movie.models import Movies
import datetime
from datetime import timedelta
from django.template.loader import render_to_string

class Command(BaseCommand):
    def handle(self, *args, **options):
        for rent in MoviesRent.objects.all():
            date = datetime.datetime.now() - rent.date_out.replace(tzinfo=None)
            if rent.date_return is None and date >= timedelta(days=14):
                print(rent.fk_movie.name + " a été loué le " + str(rent.date_out))
                



                user = {
                    'date_de_location' : rent.date_out,
                    'username' : rent.fk_client.user.username,
                    'film' : rent.fk_movie.name,
                }
                
                email_content = render_to_string('email/email_sender.html', user)

                print(email_content)