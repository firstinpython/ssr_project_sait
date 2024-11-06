from django.contrib import admin
from .models import ProjectsModel,StatusModel
# Register your models here.
admin.site.register(ProjectsModel)
admin.site.register(StatusModel)