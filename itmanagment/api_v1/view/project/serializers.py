from rest_framework import serializers
from projects.models import ProjectsModel, StatusModel
from django_filters import rest_framework as filters

class BaseFilter(filters.BaseInFilter,filters.CharFilter):
    pass

class ListFiltr(filters.FilterSet):
    ...


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name_project", "description_project", "status")
        model = ProjectsModel


class ListProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = ProjectsModel