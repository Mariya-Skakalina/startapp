
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.serializers import TagAddSerializer, TagAllSerializer
from project.models import Project, Tag


class BaseAddViews(APIView):
    parser_classes = (JSONParser,)
    model = Tag
    related_model = Project
    serializer = TagAddSerializer
    field = 'tag'

    def name_field(self, project, tag, attr):
        return getattr(project, attr).add(tag)

    def post(self, request, **kwargs):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            project = self.related_model.objects.get(id=request.data['id_project'])
            req_name = request.data['name']
            tag_name = req_name.capitalize()
            try:
                name_tag = self.model.objects.get(name=tag_name)
                self.name_field(project, name_tag, self.field)
            except self.model.DoesNotExist:
                tag = self.model(name=tag_name)
                tag.save()
                self.name_field(project, tag, self.field)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BaseAllView(APIView):
    model = Tag
    serializer = TagAllSerializer

    def name_field(self, pk):
        filter_name = self.model.objects.filter(tags__id=pk)
        return filter_name

    def get(self, request, pk, format=None):
        tags = self.name_field(pk)
        serializer = self.serializer(tags, many=True)
        return Response(serializer.data)


class BaseDelete(APIView):
    model = Tag
    related_model = Project
    field = 'tag'

    def get_object(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def name_field(self, project, tag, attr):
        return getattr(project, attr).remove(tag)

    def delete(self, request, pk, id_project, format=None):
        tag = self.get_object(pk)
        project = self.related_model.objects.get(id=id_project)
        self.name_field(project, tag, self.field)
        return Response(status=status.HTTP_204_NO_CONTENT)
