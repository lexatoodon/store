from django.shortcuts import render, get_object_or_404
from shop.models import Book, Genre, Author
from cart.forms import CartAddBooktForm
from review.models import Review
from review.forms import ReviewForm
import string


def author_list(request, start_with_letter: str = None):
    if start_with_letter:
        authors = Author.objects.filter(name__istartswith = start_with_letter )
        return render(request, 'shop/author/list.html', {'authors': authors, 'start_with_letter': start_with_letter})
    alphabet = string.ascii_lowercase
    return render(request, 'shop/author/list.html', {'alphabet': alphabet})

def author_detail(request, id ,author_slug):
    author = get_object_or_404(Author.objects.prefetch_related('books'), id = id, slug = author_slug)
    return render(request, 'shop/author/detail.html', {'author': author})


def book_list(request, genre_slug = None):
    genre = None
    genres = Genre.objects.all()
    books = Book.objects.filter(available = True)
    if genre_slug:
        genre = get_object_or_404(Genre, slug = genre_slug)
        books = books.filter(genre = genre)
    context = {'genre': genre, 'genres': genres ,'books': books}
    return render(request, 'shop/book/list.html', context)


def book_detail(request, id, book_slug):
    book = get_object_or_404(Book.objects.select_related('author').prefetch_related('genre'),
                            id=id, slug=book_slug, available=True)
    reviews = Review.objects.filter(book = book.id).select_related('user')
    cart_book_form = CartAddBooktForm()
    review_form = ReviewForm()
    context = {
        'book': book, 
        'cart_book_form': cart_book_form,
        'review_form': review_form, 
        'reviews':reviews,
        }
    return render(request,'shop/book/detail.html', context)