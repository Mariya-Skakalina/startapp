from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DateOfBirthSerializer
from user.models import User
from rest_framework.parsers import JSONParser
# Create your views here.
class DateOfBirthView(APIView):
    parser_classes = (JSONParser, )
    def post(self, request, **kwargs):
        # print(request.body)
        # print(request.data)
        # print(request.user)
        serializer = DateOfBirthSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            ids = request.user.id
            User.objects.filter(id=ids).update(age=serializer.data['age'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = DateOfBirthSerializer(user)
        return Response(serializer.data)
