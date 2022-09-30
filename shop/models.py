from django.db import models
from django.urls import reverse
from django.db.models import Avg

class Author(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to = r'authors/%Y/%m/%d', blank = True)
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name'])
        ]
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def get_absolute_url(self):
        return reverse('shop:author_detail', args=[self.id, self.slug])
        
    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['name']),
            ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:book_list_by_genre', args=[self.slug])

    def __str__(self):
        return self.name

class Book(models.Model):
    genre = models.ManyToManyField(Genre, related_name='genres')
    author = models.ForeignKey(Author, related_name='books', on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to=r'books/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    class Meta:
        ordering = ['name']
        indexes = [
        models.Index(fields=['id', 'slug']),
        models.Index(fields=['name']),
        ]

    def get_avg_rating(self):
        return self.reviews.aggregate(Avg('rating'))['rating__avg']

    def get_absolute_url(self):
        return reverse('shop:book_detail', args=[self.id ,self.slug])
    
    def __str__(self):
        return self.name