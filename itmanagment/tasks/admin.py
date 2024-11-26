from django.contrib import admin
from .models import TaskModel, StatusTaskModel, PriorityTaskModel, Comments

# Register your models here.

admin.site.register(TaskModel)
admin.site.register(StatusTaskModel)
admin.site.register(PriorityTaskModel)
admin.site.register(Comments)