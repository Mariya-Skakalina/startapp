from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DateOfBirthSerializer
from rest_framework.permissions import IsAuthenticated
from user.models import User

# Create your views here.
class DateOfBirthView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, **kwargs):
        serializer = DateOfBirthSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = DateOfBirthSerializer(user)
        return Response(serializer.data)
