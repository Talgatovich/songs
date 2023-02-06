from django.contrib import admin
from .models import Artist, Album, Song, AlbumSong


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ("name",)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
	list_display = ("title", "release_year")


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
	list_display = ("title", )


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
	list_display = ("album", "song",)