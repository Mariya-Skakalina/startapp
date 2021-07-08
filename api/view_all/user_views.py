from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.serializers import DateOfBirthSerializer
from user.models import User


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
