from rest_framework import serializers
from users.models import UsersModel, DevStackModel, ProfessionCategoryModel, RoleModel


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        fields = ("username", "first_name", "last_name", "email",
                  "age", "role", "profession_category", "dev_stack",
                  "projects", "password")
        model = UsersModel

    def create(self, validated_data):
        password = validated_data.pop('password')
        dev_stack = validated_data.pop('dev_stack', [])
        projects = validated_data.pop('projects', [])

        user = UsersModel(**validated_data)
        user.set_password(password)
        user.save()
        user.dev_stack.set(dev_stack)
        user.projects.set(projects)
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionCategoryModel
        fields = "__all__"


class DevStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevStackModel
        fields = "__all__"


class ListUserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    profession_category = CategorySerializer()
    dev_stack = DevStackSerializer(many=True)

    class Meta:
        fields =("username","first_name","last_name","email","age","role","profession_category","dev_stack")
        model = UsersModel
