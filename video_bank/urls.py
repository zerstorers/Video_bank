"""video_bank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import Settings
from movie.views import HomePageView, DetailMoviesView, CreateMoviesView, UpdateMoviesView, DeleteMoviesView
from shop.views import ClientListView, ClientDetailView, DeleteClientView, CreateClientView
from django.conf.urls.i18n import i18n_patterns


urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('accounts/', include('userena.urls'), name='account'),
    # URLS MOVIE
    path("" , HomePageView.as_view() ,name='home'),
    path("movie/detail/<int:pk>/" , DetailMoviesView.as_view() ,name='detail_movies'),
    path("movie/create/" , CreateMoviesView.as_view() ,name='create_movies'),
    path("movie/update/<int:pk>/" , UpdateMoviesView.as_view() ,name='update_movies'),
    path("movie/delete/<int:pk>/" , DeleteMoviesView.as_view() ,name='delete_movies'),
    # URLS CLIENT
    path("client/list/" , ClientListView.as_view() ,name='client_list'),
    path("client/detail/<int:pk>" , ClientDetailView.as_view() ,name='client_detail'),
    path("client/delete/<int:pk>/" , DeleteClientView.as_view() ,name='delete_client'),
    path("client/create/" , CreateClientView.as_view() ,name='create_client'),

)

urlpatterns += [
    path('i18n/', include('django.conf.urls.i18n'), name='set_language'),
]