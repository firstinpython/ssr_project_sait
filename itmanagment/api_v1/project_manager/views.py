
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