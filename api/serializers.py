from rest_framework import serializers


class DateOfBirthSerializer(serializers.Serializer):
    age = serializers.DateField()


class SkillAddSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)


class SkillAllSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
