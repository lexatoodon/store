from django.db import models
from shop.models import Book
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'reviews')
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)])
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-created']
    
    def __str__(self) -> str:
        return f"{self.user}'s review on {self.book}"
        

