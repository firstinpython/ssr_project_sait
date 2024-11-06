from django.shortcuts import render
from users.models import UsersModel
from projects.models import ProjectsModel
from django.contrib.auth.decorators import login_required
from .serializer import UserSerializer, CreateProjectSerializer,ProjectsSerializer
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
        if request.user.is_authenticated:
            if request.user.role.name_role == "РП":
                return Response("ok")
            else:
                return Response('no')
        return Response('ok')
@login_required()
@api_view(['GET','POST'])
def userprofile(request):
    if request.method == "GET":
        serializer = UserSerializer(request.user)

        return Response(
                serializer.data
        )
