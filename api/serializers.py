from rest_framework import serializers


class DateOfBirthSerializer(serializers.Serializer):
    age = serializers.DateField()


class SkillAddSerializer(serializers.Serializer):
    id_project = serializers.IntegerField()
    name = serializers.CharField(max_length=100)


class SkillAllSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


class TagAddSerializer(serializers.Serializer):
    id_project = serializers.IntegerField()
    name = serializers.CharField(max_length=250)


class TagAllSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()

class TagDeleteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
