from .models import Visit_stat
from datetime import date

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        print('plop')
        # if Visit_stat.date == date.today() and Visit_stat.url == request.META.get('REMOTE_ADDR'):
        try:

            Visit_stat.objects.create(url=request.path, ip=request.META.get('REMOTE_ADDR'), date= date.today())
        except:
            pass
        return response

    def process_template_response(self, request, response):
        response.context_data["visit_stat"] = Visit_stat.objects.all().filter(url =request.path).count()
        return response
        # Code to be executed for each request/response after
        # the view is called.


