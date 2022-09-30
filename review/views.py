from django.views.decorators.http import require_POST
from review.models import Review
from review.forms import ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from shop.models import Book
from django.urls import reverse
from django.shortcuts import redirect


@login_required
@require_POST
def add_review(request, pk):
    form = ReviewForm(request.POST)
    book = Book.objects.get(id= pk)
    if form.is_valid():
        Review.objects.create(
            book = book,
            user = request.user,
            rating = form.instance.rating,
            text = form.instance.text
        )
        messages.success(request, "Review posted!",fail_silently=True)
    return redirect(reverse('shop:book_detail', args=[pk, book.slug]))