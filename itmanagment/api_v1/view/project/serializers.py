from rest_framework import serializers
from projects.models import ProjectsModel, StatusModel


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("name_project", "description_project", "status")
        model = ProjectsModel