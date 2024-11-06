from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from users.models import UsersModel
from projects.models import ProjectsModel

class UsersSerializer(ModelSerializer):
    class Meta:
        fields = ("username","password")
        model = UsersModel

class CreateProjectSerializer(ModelSerializer):
    class Meta:
        fields = ("name_project","description_project")
        model = ProjectsModel

# class UserSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=120)
#     last_name = serializers.CharField(max_length=120)
#     avatar = serializers.FileField()
#     history_project = serializers.
#
#     def create(self, validated_data):
#         return UsersModel(**validated_data)
class UserSerializer(ModelSerializer):
    class Meta:
        fields = ("first_name","last_name","avatar")
        model = UsersModel,ProjectsModel