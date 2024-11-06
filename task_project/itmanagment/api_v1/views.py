from django.shortcuts import render
from users.models import UsersModel
from projects.models import ProjectsModel
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer, CreateProjectSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
class UserRegistr(CreateAPIView):
    queryset = UsersModel
    serializer_class = UserSerializer

class UserAuthentication():
    ...


@api_view(['GET','POST'])
def createpost(request):
    if request.method == 'POST':
        return Response('ok')
    else:
        print(request.user)
        if request.user.is_authenticated:
            if request.user.role.name_role == "РП":
                return Response("ok")
            else:
                return Response('no')
        return Response('ok')
@login_required()
@api_view(['GET','POST'])
def userprofile(request):
    first_name = request.user.first_name
    last_name = request.user.last_name
    avatar = request.user.avatar
    history_project = request.user.projects
    data = {
        'first_name':first_name,
        "last_name":last_name,
        "avatar":avatar,
        "history_project":history_project
    }
    serializer = UserSerializer(data = data)
    print(serializer)
    if serializer.is_valid():

        return Response(
            serializer.data
    )
    else:
        return Response(
            "no"
        )
