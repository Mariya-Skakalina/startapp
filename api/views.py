from .serializers import *
from user.models import User, Skill
from .view_all.base_views import BaseDelete, BaseAllView, BaseAddViews


# Вывести все навыки
class SkillAllView(BaseAllView):
    model = Skill
    serializer = SkillAllSerializer

    def name_field(self, pk):
        filter_name = self.model.objects.filter(user_skills_id=pk)
        return filter_name


# Добавить навык
class SkillAddViews(BaseAddViews):
    model = Skill
    related_model = User
    serializer = SkillAddSerializer
    field = 'skill_user'


# Удалить навык
class SkillDelete(BaseDelete):
    model = Skill
    related_model = User
    field = 'skill_user'


# Добавить тег
# class TagAddViews(APIView):
#     parser_classes = (JSONParser,)
#
#     def post(self, request, **kwargs):
#         serializer = TagAddSerializer(data=request.data)
#         if serializer.is_valid():
#             project = Project.objects.get(id=request.data['id_project'])
#             tag_name = request.data['name']
#             # tag = Tag.objects.get_or_create(name=tag_name)
#             if Tag.objects.filter(name=tag_name).exists():
#                 project.tag.add(tag_name.id)
#             else:
#                 tag = Tag(name=request.data['name'])
#                 tag.save()
#                 project.tag.add(tag)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
