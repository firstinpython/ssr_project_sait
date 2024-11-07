from django.urls import path
from .views import UserRegistr, createpost, userprofile,list_projects,create_project,retrieve_project,delete_project,archival_projects,active_projects
urlpatterns = [
    path("users",UserRegistr.as_view()),
    path("projects",createpost),
    path("archival_projects",archival_projects),
    path("active_projects",active_projects),
    path("profile",userprofile),
    path("create_project",create_project),
    path("list_projects",list_projects),
    path("project/<int:pk>/",retrieve_project),
    path("delete_project/<int:pk>/",delete_project)

    # path("projects"),
    # path("project/<str:name>/")
]