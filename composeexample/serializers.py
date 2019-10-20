from rest_framework import serializers
from composeexample.models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'
        #fields = ('id', 'name', 'email', 'messasge')