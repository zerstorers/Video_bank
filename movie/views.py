from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Movies, MovieGenre
from django.urls import reverse_lazy
from .forms import MovieInlineFormSet
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.

class HomePageView(LoginRequiredMixin, ListView):
    model = Movies


class DetailMoviesView(LoginRequiredMixin, DetailView):
    model = Movies


class CreateMoviesView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    fields = "__all__"
    model = Movies

    permission_required = ("movies.add_movies")

    def get_context_data(self, **kwargs):
        context = CreateView.get_context_data(self, **kwargs)
        context['movie_form'] = MovieInlineFormSet()
        return context

    def form_valid(self, form):
        if form.is_valid():
            self.new_movie = form.save(commit=False)

            movie_form = MovieInlineFormSet(self.request.POST, instance=self.new_movie)

            if movie_form.is_valid():
                form.save()
                movie_form.save()
                return HttpResponseRedirect(self.get_success_url())
            context = {
                'form': form,
                'movie_form': movie_form,
                }
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy("detail_movies", args=[self.new_movie.id])

class UpdateMoviesView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    fields = "__all__"
    model = Movies

    permission_required = ("moadd_movies")

    def get_context_data(self, **kwargs):

        context = UpdateView.get_context_data(self, **kwargs)
        context['movie_form'] = MovieInlineFormSet(instance=self.get_object())

        return context

    def form_valid(self, form):
        if form.is_valid():
            self.movie_updated = form.save(commit = False)
            movie_update = MovieInlineFormSet(self.request.POST, instance=self.movie_updated)
            form.save()
            movie_update.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            context = {
                'form' : form,
                'movie_update' : movie_update,
            }
            return self.render_to_response(context)

    def get_success_url(self):
        return reverse_lazy("detail_movies", args=[self.movie_updated.id])

class DeleteMoviesView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Movies
    slug_field = "id"
    success_url = reverse_lazy('home')
    permission_required = ("movies.delete_movies")