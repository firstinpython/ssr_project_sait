from django.urls import path
from .views import UserRegistr, createpost, userprofile, list_projects, create_project, retrieve_project, \
    delete_project, archival_projects, active_projects, create_user
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("users", UserRegistr.as_view()),
    path("create_user", create_user),
    path("projects", createpost),
    path("archival_projects", archival_projects),
    path("active_projects", active_projects),
    path("profile", userprofile),
    path("create_project", create_project),
    path("list_projects", list_projects),
    path("project/<int:pk>/", retrieve_project),
    path("delete_project/<int:pk>/", delete_project),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path("create_task/",create_task)

    # path("projects"),
    # path("project/<str:name>/")
]
