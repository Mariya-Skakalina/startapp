from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from user.models import User, Skill
from rest_framework.parsers import JSONParser


# Редактировать дату рождения
class DateOfBirthView(APIView):
    parser_classes = (JSONParser, )

    def post(self, request, **kwargs):
        serializer = DateOfBirthSerializer(data=request.data)
        if serializer.is_valid():
            ids = request.user.id
            User.objects.filter(id=ids).update(age=serializer.data['age'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Вывести все навыки
class SkillAllView(APIView):

    def get(self, request, format=None):
        skill = Skill.objects.all()
        serializer = SkillAllSerializer(skill, many=True)
        return Response(serializer.data)


# Добавить навык
class SkillAddViews(APIView):
    parser_classes = (JSONParser,)

    def post(self, request, **kwargs):
        serializer = SkillAddSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=request.user.id)
            Skill.objects.create(name=serializer.data['name'], user_skills=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Удалить навык
class SkillDelete(APIView):

    def get_object(self, pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        skill = self.get_object(pk)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
