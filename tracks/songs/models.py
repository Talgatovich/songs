from django.db import models


class Artist(models.Model):
	"""Исполнитель"""
	name = models.CharField("Имя исполнителя", max_length=150)

	def __str__(self):
		return f"{self.name}"


class Album(models.Model):
	"""Альбом"""
	artist = models.ForeignKey(
		"Исполнитель",
		Artist,
		on_delete=models.CASCADE,
		related_name="albums",

	)
	title = models.CharField(
		"Название альбома",
		max_length=200
	)
	release_year = models.PositiveIntegerField("Год выпуска")

	def __str__(self):
		return f"{self.title}"


class Song(models.Model):
	"""Песня"""
	title = models.CharField(
		"Название песни",
		max_length=150
	)
	number_in_album = models.ManyToManyField(through='AlbumSong')

	def __str__(self):
		return f"{self.title}"


class AlbumSong(models.Model):
	"""Промежуточная модель"""
	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	song = models.ForeignKey(Song, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.album}, {self.song}"
