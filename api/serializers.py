from rest_framework import serializers
from user.models import User


class DateOfBirthSerializer(serializers.Serializer):
    age = serializers.DateField()
