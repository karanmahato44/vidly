from django.contrib import admin
from django.urls import include, path
from . import views as movies_views

urlpatterns = [
    path('', movies_views.index, name='movies_index'),
    path('<int:movie_id>/', movies_views.detail, name='movie_detail'),
]