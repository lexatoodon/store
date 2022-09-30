from django.urls import path
from review import views

app_name = 'review'

urlpatterns = [
    path('add/<int:pk>/', views.add_review, name = 'review_add')
]