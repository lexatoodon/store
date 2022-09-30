from django.urls import path
from order import views
app_name = 'order'

urlpatterns = [
    path('', views.order_create, name = 'order_create')
]