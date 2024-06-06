from django.urls import path
from django.contrib import admin
from queri.views import movies_view
from . import views

urlpatterns = [
    path("", views.movies_view, name="movies"),
    path("movies.html/", movies_view),
]