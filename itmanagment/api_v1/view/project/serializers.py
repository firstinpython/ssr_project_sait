from rest_framework import serializers
from projects.models import ProjectsModel, StatusModel
from users.models import UsersModel


class ProjectsSerializer(serializers.ModelSerializer):
    status_name = serializers.CharField(write_only=True)
    users = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        fields = ("name_project", "description_project", "status_name", "users")
        model = ProjectsModel

    def create(self, validated_data):
        status_name = validated_data.pop("status_name")
        status = StatusModel.objects.filter(name_status=status_name).first()
        if not status:
            raise serializers.ValidationError("Статус не найден")
        users_username = validated_data.pop('users', [])
        project = ProjectsModel(status=status, **validated_data)
        project.save()
        users_usernames = []
        for username in users_username:
            users_user, _ = UsersModel.objects.get_or_create(username=username)
            print(users_user,_)
            users_usernames.append(users_user)
        project.users.set(users_usernames)
        return project


class ListProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProjectsModel


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusModel
        fields = ('name_status',)


class ProfileUserSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = ProjectsModel
        fields = ("name_project", "status")
