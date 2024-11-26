from .serializers import UsersSerializer, ListUserSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.decorators import login_required
from users.models import UsersModel
from projects.models import ProjectsModel
from api_v1.view.project.serializers import ListProjectsSerializer, ProfileUserSerializer
from rest_framework import status


@api_view(['POST'])
def create_user(request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User is created","data":serializer.data},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def list_user(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = UsersModel.objects.filter(username=request.user.username).first()
            serializer = ListUserSerializer(user)
            if serializer:
                return Response({'message': 'Все пользователи', 'data': serializer.data}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Вы не вошли в систему'}, status == status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            user = UsersModel.objects.filter(username=request.user.username).first()
            projects_user = ProjectsModel.objects.filter(users=user).all()
            serializer = ListUserSerializer(user)
            serializer_project = ProfileUserSerializer(projects_user, many=True)
            if serializer:
                return Response({'user_profile': serializer.data,
                                 'projects': serializer_project.data}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'message': 'Вы не вошли в систему'}, status=status.HTTP_403_FORBIDDEN)
