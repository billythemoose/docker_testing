from rest_framework import serializers
from composeexample.models import Users
from composeexample.models import Files

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        #fields = ('id', 'name', 'email', 'messasge')

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"