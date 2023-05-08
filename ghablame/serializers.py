
from rest_framework import serializers
from .models import *



class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        # fields = '__all__'