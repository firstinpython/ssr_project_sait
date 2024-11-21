from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .view.user.views import create_user,list_user
from .view.project.views import create_project, add_people_in_project, list_projects, delete_projects,html_addprojects
from .view.tasks.views import create_tasks,list_tasks,delete_task
# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )

urlpatterns = [
    path("users", list_user),
    # path("create_user", createpost),
    # path("projects", create_project),
    # path("archival_projects", archival_projects),
    # path("active_projects", active_projects),
    # path("profile", userprofile),
    # path("create_project", create_project),
    # path("list_projects", list_projects),
    # path("project/<int:pk>/", retrieve_project),
    # path("delete_project/<int:pk>/", delete_project),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("<int:project_id>/create_task/",create_tasks),
    path("<int:project_id>/list_tasks/",list_tasks),
    path("<int:project_id>/<int:task_id>/delete/", delete_task),
    path("<int:project_id>/addproject/",add_people_in_project),
    path("list_projects/",list_projects),
    path('<int:project_id>/delete',delete_projects),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("html/addproject/",html_addprojects)


    # path("projects"),
    # path("project/<str:name>/")
]
