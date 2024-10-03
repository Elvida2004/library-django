from django.db import models

# Create your models here.
from django.db import models

class City(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'

    def __str__(self):
        return self.title

class Publisher(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='город')

    class Meta:
        verbose_name = 'издательство'
        verbose_name_plural = 'издательства'

    def __str__(self):
        return self.title

class Genre(models.Model):
    title = models.CharField(max_length=100, verbose_name='название')

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.title

class Author(models.Model):
    lastname = models.CharField(max_length=100, verbose_name='фамилия')
    name = models.CharField(max_length=100, verbose_name='имя')
    surname = models.CharField(max_length=100, verbose_name='отчество')

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'

    def __str__(self):
        return f"{self.lastname} {self.name} {self.surname}"

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='автор')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, verbose_name='издательство')
    title = models.CharField(max_length=100, verbose_name='название')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='жанр')
    year = models.CharField(max_length=4, verbose_name='год')

    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title