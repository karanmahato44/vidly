from django.contrib import admin
from .models import Genre, Movie


class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created', )    # or use fields = ()
    list_display = ('title', 'release_year', 'genre')
    
admin.site.register(Genre, GenreAdmin)
admin.site.register(Movie, MovieAdmin)