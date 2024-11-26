from django.urls import path
from .views import registration, profile

urlpatterns = [
    path('registration/',registration),
    path('profile',profile)
]