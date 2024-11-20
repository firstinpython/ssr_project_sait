from rest_framework import serializers
from tasks.models import TaskModel,StatusTaskModel,PriorityTaskModel
from projects.models import ProjectsModel
from users.models import UsersModel



class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProjectsModel
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = StatusTaskModel
class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UsersModel
class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PriorityTaskModel
class TestSerializer(serializers.ModelSerializer):
    fields = "__all__"
    model = UsersModel



class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = "__all__"

