from rest_framework import serializers
from tasks.models import TaskModel,StatusTaskModel,PriorityTaskModel,Comments
from projects.models import ProjectsModel
from users.models import UsersModel




class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectsModel
        exclude = ("id","users")
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = StatusTaskModel
class ExecutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        exclude = ("id","password")
class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = PriorityTaskModel
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = UsersModel




class TasksSerializer(serializers.ModelSerializer):
    project_name = serializers.CharField(write_only=True)
    status_name = serializers.CharField(write_only=True)
    executor_name = serializers.CharField(write_only=True)
    priority_name = serializers.CharField(write_only=True)
    resp_for_testing_name = serializers.CharField(write_only=True)

    class Meta:
        model = TaskModel
        fields = ("name_task", "description_task", "project_name", "status_name",
                  "executor_name", "priority_name", "resp_for_testing_name", "slug_name")

    def create(self, validated_data):
        project_name = validated_data.pop("project_name")
        status_name = validated_data.pop("status_name")
        executor_name = validated_data.pop("executor_name")
        priority_name = validated_data.pop("priority_name")
        resp_for_testing_name = validated_data.pop("resp_for_testing_name")

        project = ProjectsModel.objects.filter(name_project=project_name).first()
        if not project:
            raise serializers.ValidationError("Проект не найден")
        status = StatusTaskModel.objects.filter(name_status=status_name).first()
        if not status:
            raise serializers.ValidationError("Статус не найден")
        executor = UsersModel.objects.filter(username=executor_name).first()
        if not executor:
            raise serializers.ValidationError("Такой пользователь не найден")
        priority = PriorityTaskModel.objects.filter(name_priority=priority_name).first()
        if not priority:
            raise serializers.ValidationError("Приоритет не найден")
        resp_for_testing = UsersModel.objects.filter(username=resp_for_testing_name).first()
        if not resp_for_testing:
            raise serializers.ValidationError("Такой пользователь не найден")

        task = TaskModel(
            project=project,
            status=status,
            executor=executor,
            priority=priority,
            resp_for_testing=resp_for_testing,
            **validated_data
        )
        task.save()
        return task

class ListTasksSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()
    status = StatusSerializer()
    executor = ExecutorSerializer()
    priority = PrioritySerializer()
    resp_for_testing = ExecutorSerializer()
    class Meta:
        model = TaskModel
        # exclude = ("id",)
        fields = "__all__"
class CommentTaskSerializer(serializers.ModelSerializer):
    username_name = serializers.CharField(write_only=True)
    project_name = serializers.CharField(write_only=True)
    task_name = serializers.CharField(write_only=True)
    class Meta:
        model = Comments
        fields = ('username_name', "project_name", "task_name")

    def create(self, validated_data):
        username_name = validated_data.pop("username_name")
        project_name = validated_data.pop("project_name")
        task_name = validated_data.pop("task_name")

        user = UsersModel.objects.filter(username=username_name).first()
        if not user:
            raise serializers.ValidationError("Пользователь не найден")
        project = ProjectsModel.objects.filter(name_project=project_name).first()
        if not project:
            raise serializers.ValidationError("Проект не найден")
        task = TaskModel.objects.filter(name_task=task_name).first()
        if not task:
            raise serializers.ValidationError("Задача не найдена")
        comment = Comments(username=user,project=project,task=task,**validated_data)
        comment.save()

        return comment


