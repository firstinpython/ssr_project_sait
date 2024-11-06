from django.shortcuts import render
from users.models import UsersModel
from projects.models import ProjectsModel
from .serializer import UsersSerializer, CreateProjectSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .decorators import pm
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