from .serializers import UsersSerializer, ListUserSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.auth.decorators import login_required
from users.models import UsersModel

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "done"})
        else:
            error = serializer.errors
            return Response({"message": "error", "errors": error})


@login_required()
@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
def list_user(request):
    if request.method == 'GET':
        user = UsersModel.objects.filter(username=request.user.username).first()
        print(user)
        serializer = ListUserSerializer(user)
        if serializer:
            return Response({'message':serializer.data})
        else:
            error = serializer.errors
            return Response({'message':error})