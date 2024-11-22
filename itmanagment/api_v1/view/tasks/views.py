from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from tasks.models import TaskModel
from .serializers import TasksSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from users.models import UsersModel
from projects.models import ProjectsModel


@login_required()
@api_view(['GET'])
def list_tasks(request,project_id:int) -> Response:
    if request.method == "GET":
        user = UsersModel.objects.filter(pk=request.user.id).first()
        project_model = ProjectsModel.objects.filter(pk=project_id).first()
        user_task = TaskModel.objects.filter(project=project_model,executor=user).first()
        serializer = TasksSerializer(user_task)
        return Response({"message":serializer.data})
@login_required()
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def create_tasks(request,project_id):
    if request.method == "POST":
        request.data['project'] = project_id
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "chat_lesson1",
                {
                    "type":"add_task",
                    "message":f"{request.user.username} вы добавили новое задание на проект {request.data['project']}"
                }
            )
            return Response({"message":"done"})
        else:
            error = serializer.errors
            return Response({"message":error})

@login_required()
@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def delete_task(request,project_id:int,task_id:int) -> Response:
    user = UsersModel.objects.filter(pk=request.user.id).first()
    project_model = ProjectsModel.objects.filter(pk=project_id).first()
    task = TaskModel.objects.filter(pk=task_id,project=project_model, executor=user).first()
    task.delete()
    return Response({"message":"delete item"})


