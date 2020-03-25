from django.contrib import admin
from .models import Movies, MovieGenre

# Register your models here.

class AdminMovieRender(admin.StackedInline):
    list_display = ["name", "description", "date", "category"]
    model = MovieGenre

class AdminRowMovies(admin.ModelAdmin):
    inlines = [AdminMovieRender]


admin.site.register(Movies, AdminRowMovies)
