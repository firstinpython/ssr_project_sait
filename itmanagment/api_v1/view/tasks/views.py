from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from tasks.models import TaskModel, Comments
from .serializers import TasksSerializer, CommentTaskSerializer, ListTasksSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from users.models import UsersModel
from projects.models import ProjectsModel
from .fielter import TaskFilter

@api_view(['GET'])
def list_tasks(request, project_id: int) -> Response:
    if request.user.is_authenticated:
        user = UsersModel.objects.filter(pk=request.user.id).first()
        print(user)
        project_model = ProjectsModel.objects.filter(pk=project_id).first()
        print(project_model)
        user_task = TaskModel.objects.filter(project=project_model, executor=user)
        print(user_task)
        filters_task = TaskFilter(request.query_params, queryset=user_task)
        serializer = ListTasksSerializer(filters_task.qs, many=True)
        return Response({"message": "Все задания", 'data': serializer.data}, status=status.HTTP_200_OK)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def create_tasks(request, project_id):
    request.data['project'] = project_id
    serializer = TasksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "chat_lesson1",
            {
                "type": "add_task",
                "message": f"{request.user.username} вы добавили новое задание на проект {request.data['project']}"
            }
        )
        return Response({"message": "Задание добавлено", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_task(request, project_slug, task_slug):
    if request.user.is_authenticated:
        if request.user.role.name_role == "РП":
            project = ProjectsModel.objects.filter(slug_name=project_slug).first()
            task = TaskModel.objects.filter(project=project, slug_name=task_slug).first()
            if task:
                serializer = TasksSerializer(task, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'message': 'Задача успешно обновлена', 'data': serializer.data},
                                    status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({'message': 'Задача не найдена'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'У вас нет прав на выполнение этой операции'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)



@api_view(['DELETE'])
def delete_task(request, project_id: int, task_id: int) -> Response:
    if request.user.is_authenticated:
        if request.user.role.name_role == "РП":
            user = UsersModel.objects.filter(username=request.user.username).first()
            project_model = ProjectsModel.objects.filter(pk=project_id).first()
            task = TaskModel.objects.filter(pk=task_id, project=project_model, executor=user).first()
            if task:
                task.delete()
            return Response({"message": "Задача удалена"}, status=status.HTTP_200_OK)
        return Response({'message': 'У вас нет прав на выполнение этой операции'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def get_comments(request, project_id, task_id):
    if request.user.is_authenticated:
        project = ProjectsModel.objects.filter(pk=project_id).first()
        user = UsersModel.objects.filter(username=request.user.username).first()
        comments = Comments.objects.filter(username=user, project=project, task=task_id).all()

        serializers = CommentTaskSerializer(comments, many=True)
        if serializers.data:
            return Response({'message': 'Комментарии получены', 'data': serializers.data}, status=status.HTTP_200_OK)
        return Response({'message': 'Комментарии не найдены'}, status=status.HTTP_200_OK)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def create_comments(request, project_id: int) -> Response:
    if request.user.is_authenticated:
        serializer = CommentTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            project = ProjectsModel.objects.get(pk=project_id)
            task_name = TaskModel.objects.filter(project=project).first().name_task
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f"chat_lesson1",
                {
                    "type": "add_comments",
                    "message": f"{request.user.username} на таску {task_name} добавили новый коммент"
                }
            )
            return Response({'message': 'Комментарий добавлен'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['PUT'])
def update_comments(request, project_slug, task_slug):
    if request.user.role.name_role == "РП":
        project = ProjectsModel.objects.filter(slug_name=project_slug).first()
        task = TaskModel.objects.filter(project=project, slug_name=task_slug).first()
        comment = Comments.objects.filter(project=project, task=task, slug_name=task_slug).first()
        if comment:
            serializer = TasksSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Проект успешно обновлен', 'data': serializer.data},
                                status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Проект не найден'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'message': 'У вас нет прав на выполнение этой операции'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['DELETE'])
def delete_comments(request, project_slug, task_slug, comment_slug):
    if request.user.is_authenticated:
        project = ProjectsModel.objects.filter(slug_name=project_slug).first()
        task = TaskModel.objects.filter(slug_name=task_slug).first()
        user = UsersModel.objects.filter(username=request.user.username).first()
        comment = Comments.objects.filter(username=user, slug_name=comment_slug, project=project, task=task).first()
        if comment:
            comment.delete()
            return Response({"message": "done"})
        return Response({"message": "такого комментария не существует"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)
