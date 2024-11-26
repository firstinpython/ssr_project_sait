from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from websocket import create_connection
from projects.models import ProjectsModel

from .serializers import ProjectsSerializer, ListProjectsSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from users.models import UsersModel
from .fielter import ProjectsFilter
import requests


@api_view(['GET'])
def list_projects(request):
    if request.user.is_authenticated:
        user = UsersModel.objects.filter(username=request.user.username).first()
        projects = ProjectsModel.objects.filter(users=user).all()
        print(projects)
        filter_project = ProjectsFilter(request.query_params,queryset=projects)
        serializer = ListProjectsSerializer(filter_project.qs, many=True)
        return Response({"message": "Все проекты", "data": serializer.data},status=status.HTTP_200_OK)
    else:
        return Response({"message": "Вы не вошли в систему"}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def create_project(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            if request.user.role.name_role == "РП":
                serializer = ProjectsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({"message": "Проект успешно сохранился", "data": serializer.data},
                                    status=status.HTTP_200_OK)
                return Response({"message": serializer.errors}, status=status.HTTP_404_NOT_FOUND)
            return Response({'message': 'У вас нет прав на выполнение этой операции'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['PUT'])
def update_project(request, project_slug):
    if request.user.role.name_role == "РП":
        project = ProjectsModel.objects.filter(slug_name=project_slug).first()
        if project:
            serializer = ProjectsSerializer(project, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Проект успешно обновлен', 'data': serializer.data},
                                status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'Проект не найден'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'message': 'У вас нет прав на выполнение этой операции'}, status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def add_people_in_project(request, project_id):
    if request.user.is_authenticated:
        if request.user.role.name_role == "РП":
            user = UsersModel.objects.filter(pk=1).first()
            user_project = ProjectsModel.objects.filter(pk=project_id, users=user).first()
            userjson = request.data.get("user_id")
            new_user = UsersModel.objects.filter(pk=userjson).first()

            email_new_user = new_user.email
            user_project.users.add(new_user)
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "chat_lesson1",
                {
                    'type': "add_room",
                    "message": f"{request.user.username} вы в проекте!"
                }
            )
            if email_new_user:
                send_mail(
                    "ItManament project",
                    "Привет парень, повезло ты попал в отличный проект. Больших успехов тебе.",
                    "testt3stick@yandex.ru",
                    [email_new_user],
                    fail_silently=False

                )
            return Response({"message": "Пользователь успешно добавился в проект"})
        return Response({'message': 'У вас нет прав на выполнение этой операции'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)




@api_view(['DELETE'])
def delete_projects(request, project_id: int):
    if request.user.is_authenticated:
        if request.user.role.name_role == "РП":
            project = ProjectsModel.objects.filter(pk=project_id).first()
            project.delete()
            return Response({"message":"Проект успешно был удален"}, status=status.HTTP_200_OK)
        return Response({'message': 'У вас нет прав на выполнение этой операции'}, status=status.HTTP_403_FORBIDDEN)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)


