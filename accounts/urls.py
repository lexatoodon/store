
from accounts.views import Login, RegisterUserView, ProfileUpdateView, ProfileUpdatePictureView, UpdatePassword
from django.urls import path


app_name = 'accounts'

urlpatterns = [
    path('login/', Login.as_view(), name = 'login'),
    path('register/', RegisterUserView.as_view(), name = 'register'),
    path('profile/<int:pk>/', ProfileUpdateView.as_view(), name = 'profile'),
    path('profile/<int:pk>/update/', ProfileUpdatePictureView.as_view(), name = 'profile_update'),
    path('profile/<int:pk>/change_password', UpdatePassword.as_view(), name = 'profile_change_password'),
]
