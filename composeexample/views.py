from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from composeexample.models import Users
from composeexample.serializers import UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class HelloWorld(APIView):
    def get(self, request):
        return Response('Hello World! from Django.')