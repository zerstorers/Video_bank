from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MoviesRent

# Register your models here.

class AdminMovieRender(admin.StackedInline):
    list_display = ["fk_client", "fk_movie", "date_out", "date_return"]
    model = MoviesRent

class AdminRowMovies(admin.ModelAdmin):
    inlines = [AdminMovieRender]


admin.site.register(MoviesRent)
