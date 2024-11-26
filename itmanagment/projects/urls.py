from django.urls import path
from .views import project

urlpatterns = [
    path('<int:project_id>/project/',project)
]