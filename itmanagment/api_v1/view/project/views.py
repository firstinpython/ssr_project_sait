from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import ProjectsSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from users.models import UsersModel


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
            return Response({"message":"you don`t Rp"})

