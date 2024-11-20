from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.core.mail import send_mail
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from projects.models import ProjectsModel

from .serializers import ProjectsSerializer,ListProjectsSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, login_not_required
from users.models import UsersModel



@login_required()
@api_view(['GET'])
def list_projects(request):
    projects = ProjectsModel.objects.all()
    serializer = ListProjectsSerializer(projects,many=True)
    return Response(serializer.data)
@login_required()
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def create_project(request):
    if request.method == "POST":
        if request.user.role.name_role == "РП":
            user = UsersModel.objects.filter(username=request.user.username)
            serializer = ProjectsSerializer(data=request.data)
            if serializer.is_valid():

                serializer.save()
                return Response({"message": "done"})
            else:
                error = serializer.errors
                return Response({"message": "error", "errors": error})
        else:
            return Response({"message": "you don`t Rp"})


@login_required()
@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def add_people_in_project(request, project_id):
    user = UsersModel.objects.filter(pk=request.user.id).first()
    user_project = ProjectsModel.objects.filter(pk=project_id, users=user).first()
    userjson = request.data.get("user_id")
    new_user = UsersModel.objects.filter(pk=userjson).first()
    email_newuser = new_user.email
    print(email_newuser)
    user_project.users.add(new_user)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "chat_lesson1",
        {
            'type': "add_room",
            "message": f"{request.user.username} вы в танцах!"
        }
    )
    send_mail(
        "ItManament project",
        "Привет парень, повезло ты попал в отличный проект. Больших успехов тебе.",
        "testt3stick@yandex.ru",
        [email_newuser],
        fail_silently=False

    )
    return Response({"message": "done"})



@login_required()
@api_view(['DELETE'])
def delete_projects(request,project_id:int):
    project = ProjectsModel.objects.filter(pk=project_id).first()
    project.delete()
    return Response({"message":"delete project"})
