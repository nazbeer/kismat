# users/urls.py
from django.urls import path
from .views import *

urlpatterns = [
      path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', UserDetailView.as_view(), name='profile'),
    path('password-reset/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('login/', LoginView.as_view(), name='login'),
]


