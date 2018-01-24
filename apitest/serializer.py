from rest_framework import serializers
from apitest.models import *


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
        userid = UserSerializer()
	class Meta:
                model = Task
                fields = '__all__'

