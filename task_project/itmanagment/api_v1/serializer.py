from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import UsersModel
from projects.models import ProjectsModel, StatusModel


class UsersSerializer(ModelSerializer):
    class Meta:
        fields = ("username", "password")
        model = UsersModel


class CreateProjectSerializer(ModelSerializer):
    class Meta:
        fields = ("name_project", "description_project")
        model = ProjectsModel


class StatusSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = StatusModel


class ProjectsSerializer(ModelSerializer):
    status = StatusSerializer()

    class Meta:
        fields = "__all__"
        model = ProjectsModel


class UserSerializer(ModelSerializer):
    projects = ProjectsSerializer()

    class Meta:
        fields = ("first_name", "last_name", "avatar", "projects")
        model = UsersModel
