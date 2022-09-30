from django.urls import path
from shop import views

app_name = 'shop'

urlpatterns = [
    path('', views.book_list, name = 'book_list'),
    path('<slug:genre_slug>', views.book_list, name = 'book_list_by_genre'),
    path('<int:id>/<slug:book_slug>', views.book_detail, name = 'book_detail'),
    path('authors/list/', views.author_list, name = 'author_list'),
    path('authors/list/<str:start_with_letter>/', views.author_list, name = 'author_starts_with'),
    path('authors/<int:id>/<slug:author_slug>', views.author_detail, name = 'author_detail'),

]
