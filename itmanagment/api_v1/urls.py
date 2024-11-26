from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .view.user.views import create_user, list_user, profile
from .view.project.views import create_project, add_people_in_project, list_projects, delete_projects, update_project
from .view.tasks.views import create_tasks, list_tasks, delete_task, create_comments, get_comments, delete_comments, \
    update_task, update_comments


from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://wsww.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ------------users----------------#
    path("users/", list_user),
    path("create_user/", create_user),
    path("user_profile/", profile),
    # ------------projects-------------#
    path('create_project/', create_project),
    path("<int:project_id>/addproject/", add_people_in_project),
    path("list_projects/", list_projects),
    path("<str:project_slug>/update_project", update_project),
    path('<int:project_id>/delete', delete_projects),
    # ------------tasks----------------#
    path("<int:project_id>/create_task/", create_tasks),
    path("<int:project_id>/list_tasks/", list_tasks),
    path("<int:project_id>/<int:task_id>/delete/", delete_task),
    path("<str:project_slug>/<str:task_slug>/update_task/", update_task),
    path("<str:project_slug>/<str:task_slug>/<str:comment_slug>/", update_comments),
    # ------------comments--------------#
    path("<int:project_id>/create_comment", create_comments),
    path("<int:project_id>/<int:task_id>/lists_comments/", get_comments),
    path("<str:project_slug>/<str:task_slug>/<str:comment_slug>/delete_comment/", delete_comments),
    # ------------tokens----------------#
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]
