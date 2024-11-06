from django.urls import path
from .views import UserRegistr, createpost, userprofile
urlpatterns = [
    path("users",UserRegistr.as_view()),
    path("projects",createpost),
    path("profile",userprofile),
    # path("projects"),
    # path("project/<str:name>/")
]