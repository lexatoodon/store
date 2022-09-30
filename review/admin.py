from django.contrib import admin
from review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user' , 'rating', 'created', 'updated',]
    list_filter = ['created', 'updated', 'user',]
