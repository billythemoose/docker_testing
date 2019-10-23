from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser
from rest_framework import generics
from rest_framework import status
from composeexample.models import Users
from composeexample.serializers import UserSerializer, FilesSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class HelloWorld(APIView):
    def get(self, request):
        return Response('Hello World! from Django.')

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
        file_serializer = FilesSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)