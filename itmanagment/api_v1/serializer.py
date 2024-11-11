from django.db.models import Model
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import UsersModel
from projects.models import ProjectsModel, StatusModel
# from tasks.models import TaskModel, StatusTaskModel, PriorityTaskModel


class UsersSerializer(ModelSerializer):
    class Meta:
        fields = ("username", "password")
        model = UsersModel


class UserRegistrSerializer(ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name", "last_name", "avatar", "age", "role", "profession_category")
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

    def create(self, validated_data):
        object_model = StatusModel.objects.filter(name_status=validated_data['status']['name_status'])
        if object_model:
            validated_data['status'] = object_model[0]
        else:
            validated_data['status'] = None
            return False
        return ProjectsModel.objects.create(**validated_data)

    class Meta:
        fields = "__all__"
        model = ProjectsModel
        error_messages = {'user': "you loh"}


class UserSerializer(ModelSerializer):
    projects = ProjectsSerializer(many=True, allow_null=True)

    def create(self, validated_data):
        return UsersModel.objects.create(**validated_data)

    class Meta:
        fields = ("username", "email", "first_name", "last_name", "avatar", "age", "projects")
        model = UsersModel


# class StatusTaskSerializer(ModelSerializer):
#     class Meta:
#         fields = "__all__"
#         model = StatusTaskModel
#
#
# class PriorityTaskSerializer(ModelSerializer):
#     class Meta:
#         fields = "__all__"
#         model = PriorityTaskModel
#
#
# class ExecutorSerializer(ModelSerializer):
#     class Meta:
#         fields = ("username",)
#         model = UsersModel


# class TaskSerializer(ModelSerializer):
#     project = ProjectsSerializer(many=True)
#     executor = ExecutorSerializer()
#
#     class Meta:
#         fields = "__all__"
#         model = TaskModel
