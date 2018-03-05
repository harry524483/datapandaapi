from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Auth
from .serializers import AuthSerializer

@api_view(['GET','POST'])
def userAuth(request):

    try:
        if request.method == 'POST':
            user = Auth.objects.get(username=request.data['username'])
    except Auth.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)



    if request.method == 'GET':
        users = Auth.objects.all()
        serializer = AuthSerializer(users, many=True)
        return Response(serializer.data)


    elif request.method == 'POST':
        result = Auth.objects.filter(
            username=request.data['username']
        ).filter(
            password=request.data['password']
        )

        if result.count() == 1:
            return Response(status.HTTP_302_FOUND)
        return Response(status.HTTP_204_NO_CONTENT)

