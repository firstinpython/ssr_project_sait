from rest_framework import serializers
from users.models import UsersModel, DevStackModel, ProfessionCategoryModel, RoleModel


class UsersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    name_role = serializers.CharField(write_only=True)
    name_prof_category = serializers.CharField(write_only=True)
    dev_stack = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        fields = ("username", "first_name", "last_name", "email",
                  "age", "name_role", "name_prof_category", "dev_stack",
                   "password")
        model = UsersModel

    def create(self, validated_data):
        password = validated_data.pop('password')
        dev_stack_names = validated_data.pop('dev_stack', [])
        role_name = validated_data.pop('name_role')
        name_prof_category = validated_data.pop('name_prof_category')

        role = RoleModel.objects.filter(name_role=role_name).first()
        if not role:
            raise serializers.ValidationError("Роль не найдена")
        prof_category = ProfessionCategoryModel.objects.filter(name_prof_category=name_prof_category).first()
        if not prof_category:
            raise serializers.ValidationError("Категория не найдена")
        user = UsersModel(role=role,profession_category=prof_category,**validated_data)
        user.set_password(password)
        user.save()
        dev_stacks = []
        for stack_name in dev_stack_names:
            dev_stack,_ = DevStackModel.objects.get_or_create(user_stack=stack_name)
            dev_stacks.append(dev_stack)
        user.dev_stack.set(dev_stacks)
        return user


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleModel
        fields = ("name_role",)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionCategoryModel
        fields = ("name_prof_category",)


class DevStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevStackModel
        fields = ("user_stack",)


class ListUserSerializer(serializers.ModelSerializer):
    role = RoleSerializer()
    profession_category = CategorySerializer()
    dev_stack = DevStackSerializer(many=True)


    class Meta:
        fields =("username","first_name","last_name","email","age","role","profession_category","dev_stack")
        model = UsersModel
